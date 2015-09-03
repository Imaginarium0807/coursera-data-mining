#!/usr/bin/python

import os
import sys
from collections import defaultdict

def topics_to_dict(infile):
    
    topics_dict = defaultdict(list)

    res_file = open(infile, 'r')

    for line in res_file:
        ls = line.split()
        
        if ls[0] == 'Topic:':
            topic_num = ls[1]
        else:
            topics_dict[topic_num].append([ls[0],ls[2]])
    
    res_file.close()

    return topics_dict

def write_topics_json(topics_dict, infile):
    
    json_file = os.path.splitext(infile)[0] + '.json'

    topics_json = open(json_file, 'w')
    
    #Write out the first couple lines
    topics_json.write('{\n      "name": "%s",\n      "children": [\n      {\n'    
                      % (os.path.splitext(infile)[0]))

    for i in range(len(topics_dict.keys())):
        topics_json.write('      "name": "Topic %s",\n      "children": [\n' 
                          % (str(i)))

        for j, topic in enumerate(topics_dict[str(i)]):
            
            #Last topic doesn't have a comma
            if j == len(topics_dict[str(i)])-1:
                topics_json.write('       {"name": "%s"}\n' % (topic[0]))
            else:    
                topics_json.write('       {"name": "%s"},\n' % (topic[0]))
        
        if i == len(topics_dict.keys())-1:
            topics_json.write('      ]\n      }\n   ]\n}')
        else:
            topics_json.write('      ]\n      },{\n')


    topics_json.close()

def main():
    #Get topic file name
    infile = sys.argv[1]
    #Read topics into a dictionary
    topics_dict = topics_to_dict(infile)
    #Write dictionary in json format
    write_topics_json(topics_dict, infile)

if __name__=="__main__":
    main()



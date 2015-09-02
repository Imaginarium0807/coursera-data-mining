#!/usr/bin/python

import glob
import subprocess
import os
import re

def main():
    
    for restaurant in glob.glob('*.txt'):
        
        infile = re.sub('[&*+-]*','',restaurant)
        
        outfile = os.path.splitext(infile)[0]+'_topics.dat'
        
        subprocess.call(('python ../task1/py27_ldaTopicModeling.py -f %s -o %s' % (infile, outfile)),shell=True)
        

if __name__=="__main__":
    main()



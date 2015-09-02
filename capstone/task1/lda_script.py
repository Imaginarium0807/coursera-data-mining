#!/usr/bin/python

import glob
import subprocess
import os
import re

def main():
    
    for restaurant in glob.glob('*.txt'):
        
        infile = re.sub('[&*+-]*','',restaurant)
        
        outfile = os.path.splitext(infile)[0]+'_topics.dat'
        command = 'python ../../task1/py27_ldaTopicModeling.py -f %s -o %s -K 10' % (infile, outfile)
        subprocess.call(command,shell=True)

if __name__=="__main__":
    main()



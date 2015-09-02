#!/usr/bin/python

import os
import subprocess
import re
import glob


def main():
    
    for filename in glob.glob('*.txt'):
        newfile = re.sub('[\'&*+-]*','',filename)

        os.rename(filename, newfile)

if __name__=="__main__":
    main()


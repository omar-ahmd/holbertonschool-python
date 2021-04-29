#!/usr/bin/python3

import sys


for i in range(len(sys.argv)):
    if i>0:
        print("{:d}: {:s}".format(i,sys.argv[i]))

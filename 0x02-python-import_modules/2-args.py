#!/usr/bin/python3

import sys


def main():
    arg = len(sys.argv)
    if arg == 1:
        txt = "{:d} arguments.".format(arg - 1)
        print(txt)
    elif arg == 2:
        txt = "{:d} argument:".format(arg - 1)
        print(txt)
        print("{:d}: {:s}".format(i, sys.argv[1]))
    else:
        txt = "{:d} arguments:".format(arg - 1)
        print(txt)
        for i in range(arg):
            if i > 0:
                print("{:d}: {:s}".format(i, sys.argv[i]))


if __name__ == '__main__':
    main()

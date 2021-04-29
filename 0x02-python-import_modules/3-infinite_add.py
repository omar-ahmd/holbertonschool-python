#!/usr/bin/python3

import sys


def main():
    arg = len(sys.argv)
    su = 0
    if arg >= 1:
        for i in range(1, arg):
            su += int(sys.argv[i])
    print('{}'.format(sum))


if __name__ == '__main__':
    main()

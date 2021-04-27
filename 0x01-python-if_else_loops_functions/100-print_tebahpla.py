#!/usr/bin/python3
for x in range(122, 96, -2):
    print('{:s}'.format(chr(x)), end=''))
    print('{:s}'.format(chr(x - 1 - 32)), end='')

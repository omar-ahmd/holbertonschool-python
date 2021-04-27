#!/usr/bin/python3
for x in range(0, 100):
    if int(x / 10) != x % 10 and ((x % 10) * 10 + x / 10) > x:
        if x < 89:
            print('{:02d}'.format(int(x)), end=", ")
        else:
            print('{:02d}'.format(int(x)))

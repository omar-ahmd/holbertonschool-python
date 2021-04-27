#!/usr/bin/python3
def uppercase(str):
    for x in str:
        flag = 0
        if ord(x) >= ord("a") and ord(x) <= ord("z"):
            print('{:c}'.format(ord(x) -32), end="")
        else:
            print('{:c}'.format(ord(x)), end="")
    print()

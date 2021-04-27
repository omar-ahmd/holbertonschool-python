#!/usr/bin/python3
def uppercase(str):
    for x in str:
        flag = 0
        if ord(x) >= ord("a") and ord(x) <= ord("z"):
            flag = 32
        print('{:c}'.format(ord(x) - flag), end="")
    print()

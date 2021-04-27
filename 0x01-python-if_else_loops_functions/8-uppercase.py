#!/usr/bin/python3
def uppercase(str):
    str = [chr(ord(i)-32) for i in str if (ord(i) >= ord("a") and
                                           ord(i) <= ord("z"))]
    print("".join(str))

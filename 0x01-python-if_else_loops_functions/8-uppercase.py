#!/usr/bin/python3
def uppercase(str):
    str = [chr(ord(i)-32) if (ord(i) >= ord("a") and
                              ord(i) <= ord("z"))
                          else i for i in str]
    print("".join(str))

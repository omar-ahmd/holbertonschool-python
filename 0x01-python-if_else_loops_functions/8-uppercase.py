#!/usr/bin/python3
def uppercase(str):
    str = [chr(ord(i)-32) for i in str]
    return "".join(str)

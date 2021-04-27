#!/usr/bin/python3
def remove_char_at(str, n):
    out = ""
    for x in range(len(str)):
        if x != n:
            out += str[x]
    return out

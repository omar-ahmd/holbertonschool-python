#!/usr/bin/python3


def canUnlockAll(boxes):
    si = len(boxes)
    keys = [0]
    for key in keys:
        for k in boxes[key]:
            if k < si and k not in keys:
                keys.append(k)
    if len(keys) != si:
        return False
    return True

#!/usr/bin/python3
def canUnlockAll(boxes):
    keysBool = [False for i in range(len(boxes))]
    keysBool[0] = True
    for indx in range(len(boxes)):
        for key in boxes[indx]:
            if key != indx and (key >= 0 or key <= len(boxes)):
                keysBool[key] = True
    return all(keysBool)

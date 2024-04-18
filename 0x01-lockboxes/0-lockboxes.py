#!/usr/bin/python3


def canUnlockAll(boxes):
    newKeys = [0]
    for newKey in newKeys:
        for key in boxes[newKey]:
            if key not in newKeys and key <= len(boxes):
                newKeys.append(key)
    return len(newKeys) == len(boxes)

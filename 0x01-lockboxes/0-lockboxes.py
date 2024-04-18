#!/usr/bin/python3
"""Method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened."""
    if not boxes:
        return False
    newKeys = [0]
    for newKey in newKeys:
        for key in boxes[newKey]:
            if key not in newKeys and key <= len(boxes):
                newKeys.append(key)
    return len(newKeys) == len(boxes)

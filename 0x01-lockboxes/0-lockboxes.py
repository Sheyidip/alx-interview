#!/usr/bin/python3
""" creating a lockbox
    A lockbox is a mechanism used to control access to a resources
"""


def canUnlockAll(boxes):
    """
    function for lockbox control
    """

    n = {0}
    unlocked = [False] * len(boxes)
    unlocked[0] = True  # start by unlocking the first box
    keys = boxes[0]  # start with the keys in the first box

    for i in range(len(boxes)):
        if unlocked[i]:
            for key in boxes[i]:
                if key < len(boxes) and not unlocked[key]:
                    unlocked[key] = True
                    keys.append(key)

    return all(unlocked)

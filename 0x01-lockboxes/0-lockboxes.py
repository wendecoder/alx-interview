#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    def canUnlockAll(boxes):
        x = len(boxes)
        c = 0
        for n in range(1, x):
            for y in boxes:
                if n in y:
                    c = c + 1
                    break
        if c >= x - 1:
            return True
        else:
            return False

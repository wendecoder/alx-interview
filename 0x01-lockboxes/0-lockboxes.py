#!/usr/bin/env python3

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

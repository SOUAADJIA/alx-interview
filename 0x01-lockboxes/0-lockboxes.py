#!/usr/bin/python3
"""Lockboxes problem."""


def canUnlockAll(boxes):
    """Determines if all boxes can be unlocked."""
    def collectKeys(box, available_keys):
        """Retrieve keys from the given box."""
        for key in box:
            if key not in available_keys:
                available_keys[key] = True

    available_keys = {0: True}  # Start with the first box unlocked
    unopened_boxes = []

    if len(boxes) == 0 or len(boxes) == 1:
        return True

    for i in range(len(boxes)):
        if i in available_keys:
            collectKeys(boxes[i], available_keys)
        else:
            unopened_boxes.append(i)

    for i in unopened_boxes:
        if i in available_keys:
            collectKeys(boxes[i], available_keys)
        else:
            return False

    return True

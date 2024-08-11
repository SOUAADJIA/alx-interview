#!/usr/bin/python3
"""Calculate the minimum number of operations to reach
exactly n characters using only Copy All and Paste."""


def minOperations(n):
    """Calculate the minimum operations to reach exactly n H characters."""
    operations = 0
    current_length = 1
    clipboard = 0
    can_paste = False

    while current_length < n:
        if n % current_length == 0:
            # Perform a Copy All operation
            clipboard = current_length
            operations += 1
            can_paste = True
        # Perform a Paste operation
        current_length += clipboard
        operations += 1

    return operations

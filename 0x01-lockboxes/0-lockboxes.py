def canUnlockAll(boxes):
    visited = set()  # Set to keep track of visited boxes
    queue = [0]      # Start with the first box

    while queue:
        box_index = queue.pop(0)
        if box_index not in visited:
            visited.add(box_index)
            for key in boxes[box_index]:
                if key not in visited and key < len(boxes):
                    queue.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)

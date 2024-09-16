def rotate_clockwise(list_2d: [list[list]]) -> list[list]:
    """
    Rotates a matrix like:
        1 2 3
        4 5 6
        7 8 9
    to:
        7 4 1
        8 5 2
        9 6 3
    """
    return [list(reversed(i)) for i in zip(*list_2d)]


def rotate_180(list_2d: [list[list]]) -> list[list]:
    """
    Rotates a matrix like:
        1 2 3
        4 5 6
        7 8 9
    to:
        9 8 7
        6 5 4
        3 2 1
    """
    return list(reversed([list(reversed(i)) for i in list_2d]))

# Example usage
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(rotate_clockwise(matrix))
# print(rotate_180(matrix))

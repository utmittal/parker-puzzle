##### puzzle_generator.py
# start = time.time()
# genned_peas = generate_all_puzzles(2, 2)
# print(len(genned_peas))
# end = time.time()
# print(end - start)
import copy
##### puzzle.py
# p = Puzzle(2, 2)
# p.set_piece(0, 0, PuzzlePiece(0, 1, 4, 0))
# p.set_piece(0, 1, PuzzlePiece(0, 0, 2, 1))
# p.set_piece(1, 1, PuzzlePiece(2, 0, 0, 3))
# p.set_piece(1, 0, PuzzlePiece(4, 3, 0, 0))
#
# p._debug_print()

##### puzzle_examples.py
# matt_puzzle.verify_puzzle()

##### list_2d_utils.py
# Example usage
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(rotate_clockwise(matrix))
# print(rotate_180(matrix))

from collections import Counter


def generate_permutations(elements: list, n: int):
    """Generates permutations of size n from the given elements.

    Args:
        elements: A list of elements.
        n: The desired permutation size.

    Yields:
        A generator of permutations.
    """
    perm_list = []

    def helper(perm: list, remaining_size: int, missing_elements: set):
        if remaining_size < len(missing_elements):
            return None

        if remaining_size == 0:
            return perm

        for elem in elements:
            new_miss = missing_elements - {elem}
            res = helper(perm + [elem], remaining_size - 1, new_miss)
            if res is not None:
                perm_list.append(res)

    helper([], n, set(elements))

    return perm_list


for p in generate_permutations([1, 2], 4):
    print(p)

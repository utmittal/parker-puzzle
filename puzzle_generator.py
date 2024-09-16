import time
from itertools import product

from puzzle import Puzzle


def generate_all_puzzles(rows: int, cols: int) -> list[Puzzle]:
    """
    Generate all puzzles of the given dimensions where each puzzle will have a unique set of connector layouts.
    """
    # By convention, we use 0 for edges
    max_unique_connectors = ((rows - 1) * cols) + ((cols - 1) * rows)
    print(f"Max Unique Connectors: {max_unique_connectors}")
    connectors_list = [_ for _ in range(1, max_unique_connectors + 1)]
    connector_combos = list(product(connectors_list, repeat=max_unique_connectors))
    print(f"Number of connector combos: {len(connector_combos)}")
    # print(connector_combos)

    puzzle_combos = []
    rotated_combos = set()
    for connectors in connector_combos:
        new_puzzle = Puzzle(rows, cols)
        conn_iter = iter(connectors)
        for row in range(rows):
            for col in range(cols):
                if row < rows - 1:
                    conn = next(conn_iter)
                    new_puzzle[row, col].down = conn
                    new_puzzle[row + 1, col].up = conn

                if col < cols - 1:
                    conn = next(conn_iter)
                    new_puzzle[row, col].right = conn
                    new_puzzle[row, col + 1].left = conn

        if new_puzzle not in rotated_combos:
            # print("------------------------")
            # new_puzzle._debug_print()
            # print("------------------------")

            new_puzzle.verify_puzzle()

            rotated_puzzles = new_puzzle.get_all_rotations()
            rotated_combos.update(rotated_puzzles)
            # for r in rotated_puzzles:
            #     print("------------------------")
            #     r._debug_print()
            #     print("------------------------")

            puzzle_combos.append(new_puzzle)
            # print(f"Puzzle Combos: {len(puzzle_combos)}")
            # print(f"Rotated Combos: {len(rotated_combos)}")

    return puzzle_combos

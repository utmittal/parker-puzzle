from puzzle import Puzzle


def generate_all_puzzles(side: int) -> list[Puzzle]:
    return generate_all_puzzles(side, side)


def generate_all_puzzles(rows: int, cols: int) -> list[Puzzle]:
    """
    Generate all puzzles of the given dimensions where each puzzle will have a unique set of connector layouts.
    """
    valid_puzzles = []
    max_unique_connectors = ((rows - 1) * cols) + ((cols - 1) * rows)

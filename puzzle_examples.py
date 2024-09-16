from puzzle import Puzzle, PuzzlePiece

matt_puzzle = Puzzle(5, 5,
                     pieces=[
                         [PuzzlePiece(0, 1, 1, 0), PuzzlePiece(0, 1, 2, 1), PuzzlePiece(0, 1, 5, 1),
                          PuzzlePiece(0, 3, 5, 1), PuzzlePiece(0, 0, 6, 3)],
                         [PuzzlePiece(1, 6, 7, 0), PuzzlePiece(2, 2, 5, 6), PuzzlePiece(5, 5, 2, 2),
                          PuzzlePiece(5, 4, 3, 5), PuzzlePiece(6, 0, 4, 4)],
                         [PuzzlePiece(7, 6, 7, 0), PuzzlePiece(5, 5, 5, 6), PuzzlePiece(2, 2, 4, 5),
                          PuzzlePiece(3, 3, 6, 2), PuzzlePiece(4, 0, 1, 3)],
                         [PuzzlePiece(7, 4, 4, 0), PuzzlePiece(5, 2, 3, 4), PuzzlePiece(4, 3, 2, 2),
                          PuzzlePiece(6, 3, 4, 3), PuzzlePiece(1, 0, 7, 3)],
                         [PuzzlePiece(4, 7, 0, 0), PuzzlePiece(3, 7, 0, 7), PuzzlePiece(2, 6, 0, 7),
                          PuzzlePiece(4, 1, 0, 6), PuzzlePiece(7, 0, 0, 1)]
                     ])
# matt_puzzle.verify_puzzle()

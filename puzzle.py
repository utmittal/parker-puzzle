class PuzzlePiece:
    # up, right, down, left
    __connections: tuple[int, int, int, int]

    def __init__(self, up: int, right: int, down: int, left: int):
        self.__connections = (up, right, down, left)

    def up(self):
        return self.__connections[0]

    def right(self):
        return self.__connections[1]

    def down(self):
        return self.__connections[2]

    def left(self):
        return self.__connections[3]

    def get_pretty(self) -> list[list[str]]:
        """
        Returns puzzle piece as a 4x4 2d list of characters. Example:
             00
            0  0
            0  1
             02
        This represents the connectors on each side of the puzzle. By convention, we use 00 for edge pieces, but it
        shouldn't really matter.
        """
        # pretty string
        ps = [[' ' for _ in range(4)] for _ in range(4)]

        # up connector
        up_con = list(str(self.up()).zfill(2))
        ps[0][1] = up_con[0]
        ps[0][2] = up_con[1]

        right_con = list(str(self.right()).zfill(2))
        ps[1][3] = right_con[0]
        ps[2][3] = right_con[1]

        down_con = list(str(self.down()).zfill(2))
        ps[3][1] = down_con[0]
        ps[3][2] = down_con[1]

        left_con = list(str(self.left()).zfill(2))
        ps[1][0] = left_con[0]
        ps[2][0] = left_con[1]

        return ps


class Puzzle:
    __rows: int
    __cols: int
    __pieces: list[list[PuzzlePiece | None]]

    def __init__(self, rows: int, cols: int):
        self.__rows = rows
        self.__cols = cols
        self.__pieces = [[None for _ in range(cols)] for _ in range(rows)]

    def set_piece(self, row: int, col: int, piece: PuzzlePiece):
        if self.__pieces[row][col] is not None:
            raise ValueError(f"Cannot add piece because a piece already exists at {row}, {col}.")

        self.__verify_connections(row, col, piece)
        self.__pieces[row][col] = piece

    def __verify_connections(self, row: int, col: int, piece: PuzzlePiece):
        if (abovep := self.__get_adj_piece(row, col, "above")) is not None:
            if abovep.down() != piece.up():
                raise ValueError(
                    f"Cannot add piece because it's connector ({piece.up()}) does not match the connector ("
                    f"{abovep.down()}) of the piece above.")
        if (rightp := self.__get_adj_piece(row, col, "right")) is not None:
            if rightp.left() != piece.right():
                raise ValueError(
                    f"Cannot add piece because it's connector ({piece.right()}) does not match the connector ("
                    f"{rightp.left()}) of the piece to the right.")
        if (belowp := self.__get_adj_piece(row, col, "below")) is not None:
            if belowp.up() != piece.down():
                raise ValueError(
                    f"Cannot add piece because it's connector ({piece.down()}) does not match the connector ("
                    f"{belowp.up()}) of the piece below.")
        if (leftp := self.__get_adj_piece(row, col, "left")) is not None:
            if leftp.right() != piece.left():
                raise ValueError(
                    f"Cannot add piece because it's connector ({piece.left()}) does not match the connector ("
                    f"{leftp.right()}) of the piece to the left.")

    def __get_adj_piece(self, row: int, col: int, pos: str) -> PuzzlePiece | None:
        # adp = ADjacent Piece
        if pos == "above":
            adp_row = row - 1
            adp_col = col
        elif pos == "right":
            adp_row = row
            adp_col = col + 1
        elif pos == "below":
            adp_row = row + 1
            adp_col = col
        elif pos == "left":
            adp_row = row
            adp_col = col - 1
        else:
            raise ValueError("Invalid position.")

        if adp_row == -1 or adp_col == -1 or adp_row == self.__rows or adp_col == self.__cols:
            # Piece out of bounds, i.e. nothing exists there
            return None
        else:
            # could also return none, which means there is no piece there yet
            return self.__pieces[adp_row][adp_col]

    def _debug_print(self):
        debug_print = []
        for row in self.__pieces:
            zipped_pretties = zip(*[piece.get_pretty() for piece in row])
            for tup in zipped_pretties:
                new_row = []
                for el in tup:
                    new_row.extend(el)
                debug_print.append(new_row)

        for row in debug_print:
            print(''.join(row))


p = Puzzle(2, 2)
p.set_piece(0, 0, PuzzlePiece(0, 1, 4, 0))
p.set_piece(0, 1, PuzzlePiece(0, 0, 2, 1))
p.set_piece(1, 1, PuzzlePiece(2, 0, 0, 3))
p.set_piece(1, 0, PuzzlePiece(4, 3, 0, 0))

p._debug_print()

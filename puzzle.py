import copy

from list_2d_utils import rotate_clockwise, rotate_180


class PuzzlePiece:
    # up, right, down, left
    __connections: list[int]

    def __init__(self, up: int, right: int, down: int, left: int):
        self.__connections = [up, right, down, left]

    def __str__(self):
        return f"(up: {self.up}, right: {self.right}, down: {self.down}, left: {self.left})"

    def __eq__(self, other):
        if self.__connections == other.__connections:
            return True
        else:
            return False

    def __repr__(self):
        return f"PuzzlePiece(up={self.up},right={self.right},down={self.down},left={self.left})"

    def __hash__(self):
        return hash(self.__repr__())

    @property
    def up(self):
        return self.__connections[0]

    @up.setter
    def up(self, value):
        self.__connections[0] = value

    @property
    def right(self):
        return self.__connections[1]

    @right.setter
    def right(self, value):
        self.__connections[1] = value

    @property
    def down(self):
        return self.__connections[2]

    @down.setter
    def down(self, value):
        self.__connections[2] = value

    @property
    def left(self):
        return self.__connections[3]

    @left.setter
    def left(self, value):
        self.__connections[3] = value

    def rotate_clockwise(self):
        # deque class has a built-in rotate method which would be better, but I think for a list of length 4, this is
        # more efficient because we don't pay the cost of casting to deque. Plus random access on deque is slower.
        self.__connections = self.__connections[3:] + self.__connections[:3]

    def rotate_180(self):
        self.__connections = self.__connections[2:] + self.__connections[:2]

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
        up_con = list(str(self.up).zfill(2))
        ps[0][1] = up_con[0]
        ps[0][2] = up_con[1]

        right_con = list(str(self.right).zfill(2))
        ps[1][3] = right_con[0]
        ps[2][3] = right_con[1]

        down_con = list(str(self.down).zfill(2))
        ps[3][1] = down_con[0]
        ps[3][2] = down_con[1]

        left_con = list(str(self.left).zfill(2))
        ps[1][0] = left_con[0]
        ps[2][0] = left_con[1]

        return ps


class PuzzleError(Exception):
    pass


class Puzzle:
    __rows: int
    __cols: int
    __pieces: list[list[PuzzlePiece | None]]

    def __init__(self, rows: int, cols: int, pieces: list[list[PuzzlePiece]] = None):
        self.__rows = rows
        self.__cols = cols
        if pieces is None:
            self.__pieces = [[PuzzlePiece(0, 0, 0, 0) for _ in range(cols)] for _ in range(rows)]
        else:
            self.__pieces = copy.deepcopy(pieces)

    def __getitem__(self, index):
        if type(index) != tuple or len(index) != 2:
            raise ValueError("Invalid indices.")
        return self.__pieces[index[0]][index[1]]

    def __eq__(self, other):
        if self.__pieces == other.__pieces:
            return True
        else:
            return False

    def __repr__(self):
        return (f"Puzzle(rows={self.__rows},cols={self.__cols},pieces="
                f"{[[repr(p) for p in prows] for prows in self.__pieces]})")

    def __hash__(self):
        return hash(self.__repr__())

    def set_piece(self, row: int, col: int, piece: PuzzlePiece):
        if self.__pieces[row][col] is not None:
            raise ValueError(f"Cannot add piece because a piece already exists at {row}, {col}.")

        self.__verify_connections(row, col, piece)
        self.__pieces[row][col] = piece

    def verify_puzzle(self):
        for row in range(self.__rows):
            for col in range(self.__cols):
                if row == 0:
                    if self.__pieces[row][col].up != 0:
                        raise PuzzleError(f"Piece {row}{col} {self.__pieces[row][col]} should have UP connector = 0.")
                elif row == self.__rows - 1:
                    if self.__pieces[row][col].down != 0:
                        raise PuzzleError(f"Piece {row}{col} {self.__pieces[row][col]} should have DOWN connector = 0.")
                else:
                    if self.__pieces[row][col].down != self.__pieces[row + 1][col].up:
                        raise PuzzleError(
                            f"DOWN connector of Piece {row}{col} {self.__pieces[row][col]} should be equal to UP "
                            f"Piece {row + 1}{col} {self.__pieces[row + 1][col]}")

                if col == 0:
                    if self.__pieces[row][col].left != 0:
                        raise PuzzleError(f"Piece {row}{col} {self.__pieces[row][col]} should have LEFT connector = 0.")
                elif col == self.__cols - 1:
                    if self.__pieces[row][col].right != 0:
                        raise PuzzleError(
                            f"Piece {row}{col} {self.__pieces[row][col]} should have RIGHT connector = 0.")
                else:
                    if self.__pieces[row][col].right != self.__pieces[row][col + 1].left:
                        raise PuzzleError(
                            f"RIGHT connector of Piece {row}{col} {self.__pieces[row][col]} should be equal to LEFT "
                            f"Piece {row}{col + 1} {self.__pieces[row][col + 1]}")

    def get_all_rotations(self):
        if self.__rows != self.__cols:
            rotated_pieces = rotate_180(copy.deepcopy(self.get_pieces()))
            for pieces_row in rotated_pieces:
                for piece in pieces_row:
                    piece.rotate_180()
            return [copy.deepcopy(self), Puzzle(self.__rows, self.__cols, rotated_pieces)]

        rotated_copies = [copy.deepcopy(self)]
        current = self
        for i in range(3):
            rotated_pieces = rotate_clockwise(copy.deepcopy(current.get_pieces()))
            for pieces_row in rotated_pieces:
                for piece in pieces_row:
                    piece.rotate_clockwise()
            rotation = Puzzle(current.__rows, current.__cols, rotated_pieces)
            current = rotation
            rotated_copies.append(rotation)
        return rotated_copies

    def get_pieces(self):
        return self.__pieces

    def get_rows(self):
        return self.__rows

    def get_cols(self):
        return self.__cols

    def __verify_connections(self, row: int, col: int, piece: PuzzlePiece):
        if (abovep := self.__get_adj_piece(row, col, "above")) is not None:
            if abovep.down != piece.up:
                raise ValueError(
                    f"Cannot add piece because it's connector ({piece.up}) does not match the connector ("
                    f"{abovep.down}) of the piece above.")
        if (rightp := self.__get_adj_piece(row, col, "right")) is not None:
            if rightp.left != piece.right:
                raise ValueError(
                    f"Cannot add piece because it's connector ({piece.right}) does not match the connector ("
                    f"{rightp.left}) of the piece to the right.")
        if (belowp := self.__get_adj_piece(row, col, "below")) is not None:
            if belowp.up != piece.down:
                raise ValueError(
                    f"Cannot add piece because it's connector ({piece.down}) does not match the connector ("
                    f"{belowp.up}) of the piece below.")
        if (leftp := self.__get_adj_piece(row, col, "left")) is not None:
            if leftp.right != piece.left:
                raise ValueError(
                    f"Cannot add piece because it's connector ({piece.left}) does not match the connector ("
                    f"{leftp.right}) of the piece to the left.")

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

# p = Puzzle(2, 2)
# p.set_piece(0, 0, PuzzlePiece(0, 1, 4, 0))
# p.set_piece(0, 1, PuzzlePiece(0, 0, 2, 1))
# p.set_piece(1, 1, PuzzlePiece(2, 0, 0, 3))
# p.set_piece(1, 0, PuzzlePiece(4, 3, 0, 0))
#
# p._debug_print()

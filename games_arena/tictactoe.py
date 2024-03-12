from apps.games_arena.celltakenerror import CellTakenError
from apps.games_arena.cellvalue import Cellvalues

class TicTacToe:
    def __init__(self):
        self.board = [[Cellvalues.EMPTY, Cellvalues.EMPTY, Cellvalues.EMPTY],
                      [Cellvalues.EMPTY, Cellvalues.EMPTY, Cellvalues.EMPTY],
                      [Cellvalues.EMPTY, Cellvalues.EMPTY, Cellvalues.EMPTY]]
        self.count = 0

    def get_board_cell(self, cell_number: int):
        row = (cell_number - 1) // 3
        column = (cell_number - 1) % 3
        return self.board[row][column]

    def validate_cell(self, number):
        if not self.get_board_cell(number) == Cellvalues.EMPTY:
            raise CellTakenError

    def play(self, cellNnumber: int):
        self.validate_cell(cellNnumber)
        row = (cellNnumber - 1) // 3
        column = (cellNnumber - 1) % 3
        if self.count % 2 == 0:
            self.board[row][column] = Cellvalues.X
        else:
            self.board[row][column] = Cellvalues.O
        self.count += 1

    def result(self):
        pass

class TicTacToe:
    def __init__(self):
        self.board = [[], [], []]

    def get_board_cell(self, cell_number: int):
        row = (cell_number - 1) // 3
        column = (cell_number - 1) % 3
        return self.board[row][column]

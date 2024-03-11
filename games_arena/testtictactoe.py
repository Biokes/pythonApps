from apps.games_arena.cellvalue import Cellvalues
from apps.games_arena.tictactoe import TicTacToe


class TestTictactoe:

    def test_createNewGame_allGameCellSAreEmpty(self):
        tictactoe: TicTacToe = TicTacToe()
        for number in range(1, 10):
            assert tictactoe.get_board_cell(number) == Cellvalues.EMPTY

    def test_changeCellState_cellStateIsChanged(self):
        tictactoe: TicTacToe = TicTacToe()
        tictactoe.play(1)
        assert tictactoe.get_board_cell(1) == Cellvalues.X

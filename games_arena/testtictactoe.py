from apps.games_arena.cellvalue import Cellvalues
from apps.games_arena.tictactoe import TicTacToe


class TestTictactoe:

    def test_createNewGame_gameCellSAreEmpty(self):
        tictactoe: TicTacToe = TicTacToe()
        assert tictactoe.get_board_cell(1) == Cellvalues.EMPTY

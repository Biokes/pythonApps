from apps.games_arena.cellvalue import Cellvalues
from apps.games_arena.tictactoe import TicTacToe


class TestTictactoe():

    def setUp(self):
        self.tictactoe = TicTacToe()

    def test_createNewGame_gameCellSAreEmpty(self):
        assert self.tictactoe.get_board_cell(1) == Cellvalues.EMPTY

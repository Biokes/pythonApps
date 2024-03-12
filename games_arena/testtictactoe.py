import pytest

from apps.games_arena.celltakenerror import CellTakenError
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

    def test_changeCellState_cellStatesChangeInTurns(self):
        tictactoe: TicTacToe = TicTacToe()
        tictactoe.play(1)
        assert tictactoe.get_board_cell(1) == Cellvalues.X
        tictactoe.play(5)
        assert tictactoe.get_board_cell(5) == Cellvalues.O

    def test_playOnFilledCell_raisesError(self):
        tictactoe: TicTacToe = TicTacToe()
        tictactoe.play(1)
        assert tictactoe.get_board_cell(1) == Cellvalues.X
        with pytest.raises(CellTakenError):
            tictactoe.play(1)

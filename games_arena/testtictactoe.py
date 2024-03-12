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

    def test_endGame_PlayerOne_wins_or_Draw(self):
        tictactoe: TicTacToe = TicTacToe()
        for numbers in range(1, 10):
            tictactoe.play(numbers)
        assert tictactoe.result() == "Player one wins."

    def test_putInvalidNumber_invalidNumberRaisesError(self):
        tictactoe: TicTacToe = TicTacToe()
        with pytest.raises(ValueError):
            tictactoe.play(12)
        with pytest.raises(Exception):
            tictactoe.play(":")
        tictactoe.play(1)
        tictactoe.play(2)
        tictactoe.play(9)
        tictactoe.play(5)
        tictactoe.play(6)
        tictactoe.play(8)
        assert tictactoe.result() == "Player Two wins."


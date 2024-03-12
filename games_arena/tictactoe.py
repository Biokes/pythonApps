import tkinter as display
from tkinter import simpledialog, messagebox

from apps.games_arena.celltakenerror import CellTakenError
from apps.games_arena.cellvalue import Cell_Values



class TicTacToe:
    root = display.Tk()
    root.withdraw()

    def __init__(self):
        self.game_board = [[Cell_Values.EMPTY, Cell_Values.EMPTY, Cell_Values.EMPTY],
                           [Cell_Values.EMPTY, Cell_Values.EMPTY, Cell_Values.EMPTY],
                           [Cell_Values.EMPTY, Cell_Values.EMPTY, Cell_Values.EMPTY]]
        self.count = 0

    def get_board_cell(self, cell_number: int):
        row = (cell_number - 1) // 3
        column = (cell_number - 1) % 3
        return self.game_board[row][column]

    def validate_cell(self, number):
        if not self.get_board_cell(number) == Cell_Values.EMPTY:
            raise CellTakenError

    def play(self, cell_number: int):
        self.validate_cell(cell_number)
        row = (cell_number - 1) // 3
        column = (cell_number - 1) % 3
        if self.count % 2 == 0:
            self.game_board[row][column] = "X"
        else:
            self.game_board[row][column] = "O"
        self.count += 1

    def result(self):
        if self.game_board[0][0] == Cell_Values.X and self.game_board[0][1] == Cell_Values.X and self.game_board[0][
            2] == Cell_Values.X:
            return "Player one wins."
        elif self.game_board[1][0] == Cell_Values.X and self.game_board[1][1] == Cell_Values.X and self.game_board[1][
            1] == Cell_Values.X:
            return "Player one wins."
        elif self.game_board[2][0] == Cell_Values.X and self.game_board[2][1] == Cell_Values.X and self.game_board[2][
            2] == Cell_Values.X:
            return "Player one wins."
        elif self.game_board[0][0] == Cell_Values.X and self.game_board[1][0] == Cell_Values.X and self.game_board[2][
            0] == Cell_Values.X:
            return "Player one wins."
        elif self.game_board[0][1] == Cell_Values.X and self.game_board[1][1] == Cell_Values.X and self.game_board[2][
            1] == Cell_Values.X:
            return "Player one wins."
        elif self.game_board[0][2] == Cell_Values.X and self.game_board[1][2] == Cell_Values.X and self.game_board[2][
            2] == Cell_Values.X:
            return "Player one wins."
        elif self.game_board[0][0] == Cell_Values.X and self.game_board[1][1] == Cell_Values.X and self.game_board[2][
            2] == Cell_Values.X:
            return "Player one wins."
        elif self.game_board[2][0] == Cell_Values.X and self.game_board[1][1] == Cell_Values.X and self.game_board[0][
            2] == Cell_Values.X:
            return "Player one wins."
        elif self.game_board[0][0] == Cell_Values.O and self.game_board[0][1] == Cell_Values.O and self.game_board[0][
            2] == Cell_Values.O:
            return "Player Two wins."
        elif self.game_board[1][0] == Cell_Values.O and self.game_board[1][1] == Cell_Values.O and self.game_board[1][
            1] == Cell_Values.O:
            return "Player Two wins."
        elif self.game_board[2][0] == Cell_Values.O and self.game_board[2][1] == Cell_Values.O and self.game_board[2][
            2] == Cell_Values.O:
            return "Player Two wins."
        elif self.game_board[0][0] == Cell_Values.O and self.game_board[1][0] == Cell_Values.O and self.game_board[2][
            0] == Cell_Values.O:
            return "Player Two wins."
        elif self.game_board[0][1] == Cell_Values.O and self.game_board[1][1] == Cell_Values.O and self.game_board[2][
            1] == Cell_Values.O:
            return "Player Two wins."
        elif self.game_board[0][2] == Cell_Values.O and self.game_board[1][2] == Cell_Values.O and self.game_board[2][
            2] == Cell_Values.O:
            return "Player Two wins."
        elif self.game_board[0][0] == Cell_Values.O and self.game_board[1][1] == Cell_Values.O and self.game_board[2][
            2] == Cell_Values.O:
            return "Player Two wins."
        elif self.game_board[2][0] == Cell_Values.O and self.game_board[1][1] == Cell_Values.O and self.game_board[0][
            2] == Cell_Values.O:
            return "Player Two wins."
        pass

    def player_one(self):
        try:
            choice = int(simpledialog.askstring("Player One Turn", "Enter a number between 1 and 9"))
            while choice < 1 or choice > 9:
                self.player_one()
            self.validate_cell(choice)
            return choice
        except AttributeError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_one()
        except CellTakenError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_one()
        except TypeError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_two()
        except ValueError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_one()
        except Exception:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_one()

    def __str__(self):
        output = f"{"-"} {"-"} {"-"} {"-"} {"-"} {"-"} {"-"} {"-"}\n"
        for row in range(3):
            for column in range(3):
                if self.game_board[row][column] == Cell_Values.EMPTY:
                    output += f" {"  "} {" | "}"
                else:
                    output += f" {self.game_board[row][column]} {" | "}"
            output += f"\n {"-"} {"-"} {"-"} {"-"} {"-"} {"-"} {"-"} {"-"}\n"
        return output

    def display_board(self):
        return f"{self.display_numbers()}\n{self.__str__()}"

    def player_two(self):
        try:
            choice = int(simpledialog.askstring("Player Two Turn", "Enter a number between 1 and 9"))
            while choice < 1 or choice > 9:
                choice = simpledialog.askinteger("Player Two Turn", "Enter a VALID NUMBER  BETWEEN 1 AND 9")
            self.validate_cell(choice)
            return choice
        except AttributeError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_two()
        except CellTakenError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_two()
        except ValueError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_two()
        except TypeError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_two()
        except Exception:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_two()

    def display_numbers(self):
        string = ""
        for numbers in range(9):
            if numbers % 3 == 0:
                string += "\n| "
            string += f" {numbers + 1} |"
        return string

    def start_game(self):
        while self.result() is not None or self.count != 9:
            messagebox.showinfo("Board", f" {self.display_board()}")
            if self.result() is not None:
                break
            self.play(self.player_one())
            messagebox.showinfo("Board", f"{self.display_board()}")
            self.play(self.player_two())
        winner = self.result()
        messagebox.showinfo("Winner", f"{winner}")


if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()

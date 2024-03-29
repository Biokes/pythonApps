class television:
    is_on = False
    station_number = 1
    volume = 0

    def __init__(self):
        self.is_on = False
        self.station_number = 1
        self.volume = 0

    def if_its_on(self):
        return self.is_on

    def toggle(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def next_station(self):
        if not self.is_on:
            return "The tv is currently off😒😒"
        if self.station_number >= 31:
            self.station_number = 1
        self.station_number += 1
        return f"station {self.station_number}"

    def previous_station(self):
        self.station_number -= 1
        if not self.is_on:
            return "The tv is currently off😒😒"
        elif self.station_number - 1 == 0:
            self.station_number = 30
        return f"station {self.station_number}"

    def check_volume(self):
        if not self.is_on:
            return "The tv is currently off😒😒"
        elif self.volume > 60:
            return f"Max volume : 60"

        return f"volume : {self.volume}"

    def increase_volume(self):
        self.volume += 1
        if not self.is_on:
            return "The tv is currently off😒😒"
        elif self.volume > 61:
            return "Max volume : 60"
        return f"volume : {self.volume}"

    def decrease_volume(self):
        self.volume -= 1
        if not self.is_on:
            return "The tv is currently off😒😒"
        elif self.volume <= 0:
            return f"Min volume : 0"
        return f"volume : {self.volume}"
import tkinter as tk
from tkinter import messagebox

def show_info_dialog(message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Information", message)
    root.destroy()  # Destroy the hidden window after displaying the message

def show_input_dialog(prompt):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    user_input = tk.simpledialog.askstring("Enter a number: ", prompt)
    messagebox.showinfo("Invalid name:")
    root.command("Enter name: ")
    root.destroy()
    return user_input

# Example usage:
show_info_dialog("This is an information message.")
user_input = show_input_dialog("Enter your name:")
if user_input:
    print("Hello,", user_input)
else:
    print("No input provided.")

if __name__ == '__main__':
    display = tk.Tk()
    tk.messagebox
    user_input = tk.Message.askString("Enter your name:")
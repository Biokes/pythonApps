import sys
import tkinter as display
from tkinter import simpledialog, messagebox

from apps.diarymodule.diaries import Diaries
from apps.diarymodule.diary import Diary
from apps.diarymodule.entryNotFoundException import EntryNotFoundError
from apps.diarymodule.incorrectpassworderror import IncorrectPasswordError
from apps.diarymodule.invalidCommandError import InvalidCommandError, UnlockDiary
from apps.diarymodule.invalidid import UsernameNotFound, InvalidId
from apps.diarymodule.namealreadyexisterror import NameAlreadyExistError


class DiaryMain:
    def __init__(self):
        self.root = display.Tk()
        self.root.withdraw()
        self.diaries: Diaries = Diaries()
        self.diary: Diary = Diary("", "")

    def landing_page(self):
        option = simpledialog.askstring("Home page", """
        select for the following options
        1. Create Diary
        2. Find Diary By username
        3. Delete Diary
        4. Exit""")
        match option:
            case "1":
                self.createDiary()
            case "2":
                self.findDiaryByUsername()
            case "3":
                self.deleteDiary()
            case "4":
                sys.exit(0)
            case _:
                self.landing_page()

    def createDiary(self):
        try:
            name = simpledialog.askstring("😘😘😘", "Pls Enter a valid username for your diary")
            password = simpledialog.askstring("Password", "Enter a valid password for your diary")
            self.diary = Diary(name, password)
            self.diaries.add(self.diary)
            messagebox.showinfo("Successful", "Diary created successfully.")
            self.diary_menu()
        except InvalidCommandError:
            messagebox.showinfo("Warning", "Invalid username or pass word entered.\nEnter a valid name and password.")
            self.createDiary()

    def findDiaryByUsername(self):
        try:
            username = simpledialog.askstring("Find Diary By UserName", "Enter Diary Username")
            self.diary = self.diaries.find_by_username(username)
            self.diary_menu()
        except UsernameNotFound:
            messagebox.showinfo("Warning", "Invalid username or pass word entered.\nEnter a valid name and password.")
            self.landing_page()

    def diary_menu(self):
        try:
            response = simpledialog.askstring("MainMenu", """
            1. Create Entry
            2. Update Entry
            3. Delete Entry
            4. Main menu
            5. Exit
            """)
            match response:
                case "1":
                    self.createEntry()
                case "2":
                    self.update_Entry()
                case "3":
                    self.delete_Entry()
                case "4":
                    self.landing_page()
                case "5":
                    messagebox.showinfo("Exit", "Exiting...........")
                    sys.exit(0)
                case _:
                    messagebox.showinfo("Invalid Choice", "You wan Enter Wrong input abi?\nIdiot😡😡😡😡😡😡")
                    self.diary_menu()
        except (IncorrectPasswordError, UnlockDiary, InvalidCommandError,
                UsernameNotFound, InvalidId, NameAlreadyExistError):
            messagebox.showinfo("Invalid Choice", "You wan Enter Wrong input abi?\nIdiot😡😡😡😡😡😡")
            self.diary_menu()

    def createEntry(self):
        entry_title = simpledialog.askstring("Entry Title", "Pls Enter Your Entry Title ")
        entry_body = simpledialog.askstring("Entry Body", "Enter Entry body")
        if len(entry_title) == 0 or len(entry_body) == 0:
            messagebox.showinfo("Warning", "Entry Title or Body cannot be Empty.")
            self.createEntry()
        entry = self.diary.create_entry(entry_title, entry_body)
        messagebox.showinfo("Successful", entry.__str__())
        self.diary_menu()

    def update_Entry(self):
        try:
            password = simpledialog.askstring("unlock Diary", "Enter Diary password: ")
            self.diary.unlock_diary(password)
            title = simpledialog.askstring("update Entry", "Enter Entry name to updated: ")
            body = simpledialog.askstring("Update Entry Body", "Enter your message")
            self.diary.updateEntry(body, title)
            self.diary_menu()
        except InvalidCommandError:
            messagebox.showinfo("Warning", "Invalid password.")
            self.diary_menu()
        except ValueError:
            messagebox.showinfo("Warning", "Invalid character for id.")
            self.diary_menu()
        except IncorrectPasswordError:
            messagebox.showinfo("Warning", "Invalid password.")
            self.diary_menu()
        except UnlockDiary:
            messagebox.showinfo("Warning", "Invalid character for id.")
            self.diary_menu()
        except EntryNotFoundError:
            messagebox.showinfo("Warning", "Invalid password.")
            self.diary_menu()

    def delete_Entry(self):
        try:
            password = simpledialog.askstring("unlock Diary", "Enter Diary password: ")
            self.diary.unlock_diary(password)
            id_number = simpledialog.askinteger("Delete Entry", "Pls Enter the Entry id")
            response = self.diary.deleteEntry(id_number)
            messagebox.showinfo("Delete Entry", response)
            self.diary_menu()
        except InvalidCommandError:
            messagebox.showinfo("Warning", "Invalid password.")
            self.delete_Entry()
        except ValueError:
            messagebox.showinfo("Warning", "Invalid character for id.")
            self.delete_Entry()
        except IncorrectPasswordError:
            messagebox.showinfo("Warning", "Invalid password.")
            self.delete_Entry()
        except UnlockDiary:
            messagebox.showinfo("Warning", "Invalid character for id.")
            self.delete_Entry()
        except EntryNotFoundError:
            messagebox.showinfo("Warning", "Invalid password.")
            self.delete_Entry()

    def deleteDiary(self):
        try:
            username = simpledialog.askstring("Delete Diary", "Enter Diary UserName")
            password = simpledialog.askstring("Delete Diary", "Enter Diary Password")
            self.diaries.delete_diary(username, password)
            messagebox.showinfo("Delete Diary", "Diary Deleted successfully")
            self.landing_page()
        except InvalidCommandError as error:
            messagebox.showerror("Delete Diary", f"{error}")
            self.landing_page()


if __name__ == "__main__":
    mainApp = DiaryMain()
    mainApp.landing_page()

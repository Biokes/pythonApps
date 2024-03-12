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

    def createDiary(self):
        try:
            name = simpledialog.askstring("Create Diary", "Pls Enter a valid username for your diary")
            password = simpledialog.askstring("Enter Password",
                                              "Enter a valid password for your diary\n Note if Forgotten Diary Cannot be Retrieved")
            self.diary = Diary(name, password)
            self.diary.lock_diary()
            self.diaries.add(self.diary)
            messagebox.showinfo("Successful", "Diary created successfully.\n Diary is Now Locked.")
            self.diary_menu()
        except InvalidCommandError:
            messagebox.showinfo("Warning", "Invalid username or Password entered.\nEnter a valid name and password.")
            self.diary_menu()
        except NameAlreadyExistError:
            messagebox.showerror("Error", "Username already Exist")

    def findDiaryByUsername(self):
        try:
            username = simpledialog.askstring("Find Diary By UserName", "Enter Diary Username")
            self.diary = self.diaries.find_by_username(username)
            self.diary_menu()
        except UsernameNotFound:
            messagebox.showinfo("Warning", "Invalid username\nUserName Does not match any Existing Diary UserName.")
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
            messagebox.showinfo("Invalid Choice", "Wrong set of Information's provided\nPlease check and retry.")
            self.diary_menu()

    def createEntry(self):
        try:
            diary_password = simpledialog.askstring("Entry Title", "Pls Enter Your Password")
            self.diary.unlock_diary(diary_password)
            entry_title = simpledialog.askstring("Entry Title", "Pls Enter Your Entry Title ")
            entry_body = simpledialog.askstring("Entry Body", "Enter Entry body")
            if len(entry_title) == 0 or len(entry_body) == 0:
                messagebox.showinfo("Warning", "Entry Title or Body cannot be Empty.")
                self.createEntry()
            entry = self.diary.create_entry(entry_title, entry_body)
            messagebox.showinfo("Successful", entry.__str__())
            self.diary.lock_diary()
            self.diary_menu()
        except (IncorrectPasswordError, UnlockDiary, InvalidCommandError,
                UsernameNotFound, InvalidId, NameAlreadyExistError) as error:
            messagebox.showinfo("Warning", f"{error}\nPlease check and retry.")
            self.diary_menu()

    def update_Entry(self):
        try:
            password = simpledialog.askstring("unlock Diary", "Enter Diary password: ")
            self.diary.unlock_diary(password)
            title = simpledialog.askstring("update Entry", "Enter Entry name to updated: ")
            body = simpledialog.askstring("Update Entry Body", "Enter your message")
            self.diary.updateEntry(body, title)
            self.diary.lock_diary()
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
            messagebox.showinfo("Delete Entry", f"{response}\n Diary is now Locked.")
            self.diary.lock_diary()
            self.diary_menu()
        except InvalidCommandError:
            messagebox.showinfo("Warning", "Invalid UserName orPassword.")
            self.delete_Entry()
        except ValueError:
            messagebox.showinfo("Warning", "Invalid character for id.")
            self.diary_menu()
        except IncorrectPasswordError:
            messagebox.showinfo("Warning", "Invalid password.")
            self.diary_menu()
        except UnlockDiary:
            messagebox.showinfo("Warning", "Diary is Locked\nEnter The correct password to unlock.")
            self.diary_menu()
        except EntryNotFoundError:
            messagebox.showinfo("Warning", "Invalid password.")
            self.diary_menu()


if __name__ == "__main__":
    mainApp = DiaryMain()
    mainApp.landing_page()

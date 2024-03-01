from apps.diary.Entry import Entry
from apps.diary.invalidCommandException import InvalidCommandException


class Diary:

    def __init__(self, name: str, password: str):
        if len(name.strip()) == 0:
            raise InvalidCommandException
        self.name = name
        if len(password) == 0:
            raise InvalidCommandException
        self.entries = []

    def isLocked(self):
        return True

    def number_of_entries(self):
        return len(self.entries)

    def createEntry(self, title: str, body: str):
        entry = Entry(title, body)
        self.entries.append(entry)


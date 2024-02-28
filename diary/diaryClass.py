from apps.diary.IdNotFoundException import IdNotFoundException
from apps.diary.entryNotFoundException import EntryNotFoundException
from apps.diary.incorrectPasswordException import IncorrectPasswordException
from apps.diary.invalidCommandException import InvalidCommandException

from apps.diary.Entry import Entry


class Diary:

    def __init__(self, name: str, password: str):
        if len(name.strip()) == 0:
            raise InvalidCommandException
        self.name = name
        if len(password) == 0:
            raise InvalidCommandException
        self.password = password
        self.entries = []
        self.isLocked = False

    def unlock_diary(self, password: str):
        if password == self.password:
            self.isLocked = False
            pass
        raise IncorrectPasswordException

    def number_of_entries(self):
        return len(self.entries)

    def lock_diary(self):
        self.isLocked = True
        pass

    def isLocked(self) -> bool:
        return self.isLocked

    def createEntry(self, title: str, body: str):
        entry: Entry = Entry(title, body)
        self.entries.append(entry)
        pass

    def deleteEntry(self, idNumber: int):
        if not self.isLocked:
            for entry in self.entries:
                if entry.getId() == idNumber:
                    self.entries.remove(entry)
                    pass
            raise IdNotFoundException
        raise IncorrectPasswordException

    def findEntryById(self, idNumber: int):
        if not self.isLocked:
            for entry in self.entries:
                if entry.getId() == idNumber:
                    return entry
            raise EntryNotFoundException
        raise IncorrectPasswordException

    def updateEntry(self, idNumber: int, title: str, body: str):
        if not self.isLocked:
            self.findEntryById(idNumber).setBody(body).setTitle(title)
            pass
        raise IncorrectPasswordException

    def getName(self):
        return self.name

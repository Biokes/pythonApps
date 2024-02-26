from diary.Entry import Entry
from diary.IdNotFoundException import IdNotFoundException
from diary.entryNotFoundException import EntryNotFoundException
from diary.incorrectPasswordException import IncorrectPasswordException
from diary.invalidCommandException import InvalidCommandException


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

    def unlockDiary(self, password: str):
        if password == self.password:
            self.isLocked = False
            pass
        raise IncorrectPasswordException

    def numberOfEntries(self):
        return len(self.entries)

    def lockDiary(self):
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

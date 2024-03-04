from apps.diarymodule.Entry import Entry
from apps.diarymodule.entryNotFoundException import EntryNotFoundError
from apps.diarymodule.incorrectpassworderror import IncorrectPasswordError
from apps.diarymodule.invalidCommandException import UnlockDiary


class Diary:
    def __init__(self, username: str, password):
        self.is_lock = True
        self.name = username
        self.password = password
        self.entries = []

    def is_locked(self) -> bool:
        return self.is_lock

    def unlock_diary(self, password):
        if self.password == password:
            self.is_lock = False
            return
        raise IncorrectPasswordError

    def lock_diary(self):
        self.is_lock = True
        pass

    def create_entry(self, entry_title: str, entry_body):
        entry: Entry = Entry(len(self.entries) + 101, entry_title, entry_body)
        self.entries.append(entry)
        pass

    def number_of_entries(self) -> int:
        return len(self.entries)

    def find_entry_by_id(self, entry_id_number: int) -> Entry:
        if not self.is_lock:
            for entries in self.entries:
                if entries.get_entry_id() == entry_id_number:
                    return entries
            raise EntryNotFoundError

    def deleteEntry(self, entry_id_number: int):
        if self.is_lock:
            self.entries.remove(self.find_entry_by_id(entry_id_number))
            return "Entry deleted successfully"
        else:
            raise UnlockDiary

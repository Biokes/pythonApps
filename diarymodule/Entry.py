from datetime import date

from apps.diarymodule.invalidid import InvalidId


class Entry:
    def validate_id(self, id_number):
        if id_number < 1:
            raise InvalidId
        self.id = id_number

    def __init__(self, id_number: int, title: str, body: str):
        self.id = 0
        self.validate_id(id_number)
        self.title = title
        self.body = body
        self.date_created = date.today()

    def get_entry_id(self):
        return self.id

    def __str__(self):
        return f"Entry ID : {self.id}\nTitle : {self.title}\nBody : {self.body}\nDate Created : {self.date_created}"

    def get_entry_title(self):
        return self.title

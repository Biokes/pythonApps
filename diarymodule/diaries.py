from apps.diarymodule.diary import Diary
from apps.diarymodule.invalidCommandError import InvalidCommandError
from apps.diarymodule.invalidid import UsernameNotFound
from apps.diarymodule.namealreadyexisterror import NameAlreadyExistError


class Diaries:
    def add(self, diary_to_be_added: Diary):
        self.__validatenameAndPassword(diary_to_be_added)
        self.list_of_diaries.append(diary_to_be_added)
        return

    def __init__(self):
        self.list_of_diaries = []
        self.diary_names = []

    def length(self) -> int:
        return len(self.list_of_diaries)

    def __validatenameAndPassword(self, diary: Diary):
        if diary.username() in self.diary_names:
            raise NameAlreadyExistError
        if len(diary.username()) == 0:
            raise InvalidCommandError
        if diary.passwordLength() == 0:
            raise InvalidCommandError
        self.diary_names.append(diary.username())

    def find_by_username(self, username: str) -> Diary:
        for diary in self.list_of_diaries:
            if diary.username() == username:
                return diary
        raise UsernameNotFound

    def delete_diary(self, diary_username: str, password: str):
        for diary in self.list_of_diaries:
            if diary.username() == diary_username:
                if diary.isCorrectPassword(password):
                    self.list_of_diaries.remove(diary)
                    return
                raise InvalidCommandError
        raise InvalidCommandError

from diary.diaryClass import Diary


class DiaryNotfoundError:
    pass


class Diaries:

    def __init__(self):
        self.diaries = []

    def addDiary(self, username: str, password: str):
        diary: Diary = Diary(username, password)
        self.diaries.append(diary)
        pass

    def findByUserName(self, username: str):
        for diary in self.diaries:
            if diary.getName() == username:
                return diary
        raise DiaryNotfoundError

    def deleteDiary(self, username: str):
        for diary in self.diaries:
            if diary.getName() == username:
                self.diaries.remove(diary)
                pass
        raise DiaryNotfoundError

from apps.diarymodule.diaryClass import Diary


class TestDiary:
    def test_DiaryIsLockedAfterCreation(self):
        diary: Diary = Diary("name", "password")
        assert diary.isLocked()

    def test_diary_can_create_entry(self):
        diary: Diary = Diary("name", "username")
        assert diary.number_of_entries() == 0

    def test_create_entry_test_diary_entry_size_increases(self):
        diary: Diary = Diary("name", "password")
        diary.createEntry("title", "body")
        assert diary.number_of_entries() == 1

    def test_entry_can_be_created_and_deleted(self):
        diary: Diary = Diary("name", "password")
        diary.createEntry("title", "body")
        assert diary.number_of_entries() == 1
        diary.deleteEntry(100101)

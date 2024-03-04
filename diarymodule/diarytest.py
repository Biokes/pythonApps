from datetime import date

import pytest

from apps.diarymodule.Entry import Entry
from apps.diarymodule.diaries import Diaries
from apps.diarymodule.diary import Diary
from apps.diarymodule.entryNotFoundException import EntryNotFoundError
from apps.diarymodule.incorrectpassworderror import IncorrectPasswordError
from apps.diarymodule.invalidCommandException import UnlockDiary
from apps.diarymodule.invalididerror import InvalidId


class TestDiary:

    def test_entry_details_can_be_gotten(self):
        entry = Entry(1234, "name", "title")
        result: str = f"Entry ID : 1234\nTitle : name\nBody : title\nDate Created : {date.today()}"
        assert entry.__str__() == result

    def test_entry_invalid_id_number_throws_error(self):
        with pytest.raises(InvalidId):
            Entry(-1234, "name", "title")
        with pytest.raises(InvalidId):
            Entry(0, "name", "title")
        Entry(12, "name", "title")

    def test_diaryIsLockedAfterCreated(self):
        diary: Diary = Diary("username", "password")
        assert diary.is_locked()

    def test_diary_is_unlocked_when_user_unlocks_diary(self):
        diary: Diary = Diary("username", "password")
        diary.unlock_diary("password")
        assert not diary.is_locked()

    def test_incorrect_password_raises_error(self):
        diary: Diary = Diary("username", "password")
        assert diary.is_locked()
        diary.lock_diary()
        with pytest.raises(IncorrectPasswordError):
            diary.unlock_diary("password1")
        diary.unlock_diary("password")
        assert not diary.is_locked()

    def test_lock_diary_check_diary_is_lock(self):
        diary: Diary = Diary("username", "password")
        assert diary.is_locked()
        diary.lock_diary()
        assert diary.is_locked()

    def test_createEntry_EntryIsCreated(self):
        diary: Diary = Diary("name", "password")
        diary.create_entry("title", "body")
        assert diary.number_of_entries() == 1

    def test_createMultipleEntries_multipleEntriesAreCreated(self):
        diary: Diary = Diary("name", "password")
        diary.create_entry("title", "body")
        assert diary.number_of_entries() == 1
        diary.create_entry("title", "body")
        diary.create_entry("title", "body")
        assert diary.number_of_entries() == 3

    def test_createDiaryAndLock_DiaryIsCreatedAndLocked(self):
        diary = Diary("name", "password")
        diary.create_entry("name", "password")
        diary.lock_diary()
        assert diary.is_locked()

    def test_EntryIsCreatedLockedUnlocked_diaryIsUnlocked(self):
        diary = Diary("name", "password")
        diary.create_entry("name", "password")
        diary.lock_diary()
        assert diary.is_locked()
        diary.unlock_diary("password")
        assert not diary.is_locked()

    def test_EntryIsCreatedLockedUnlockedWithWrongPassword_diaryIsLockedErrorIsRaised(self):
        diary = Diary("name", "password")
        diary.create_entry("name", "password")
        assert diary.is_locked()
        with pytest.raises(IncorrectPasswordError):
            diary.unlock_diary("pass wor")
        diary.unlock_diary("password")
        assert not diary.is_locked()
        diary.lock_diary()
        assert diary.is_locked()

    def test_findEntry_entryIsFoundById(self):
        diary = Diary("name", "password")
        diary.create_entry("name", "body")
        diary.unlock_diary("password")
        assert diary.find_entry_by_id(101).get_entry_title() == "name"

    def test_findInvalidEntryId_entryIsNotFound_errorIsShown(self):
        diary = Diary("name", "password")
        diary.create_entry("name", "body")
        diary.lock_diary()
        assert diary.is_locked()
        diary.unlock_diary("password")
        assert not diary.is_locked()
        with pytest.raises(EntryNotFoundError):
            diary.find_entry_by_id(109)

    def test_findEntry_returnsEntry_doesNotRemoveEntry(self):
        diary = Diary("name", "password")
        diary.create_entry("name", "body")
        diary.lock_diary()
        assert diary.is_locked()
        diary.unlock_diary("password")
        assert not diary.is_locked()
        with pytest.raises(EntryNotFoundError):
            diary.find_entry_by_id(109)
        assert diary.number_of_entries() == 1

    def test_findEntry_returnsEntry_whenDiaryIsNotLocked(self):
        diary = Diary("name", "password")
        diary.create_entry("name", "body")
        assert diary.is_locked()
        diary.unlock_diary("password")
        assert not diary.is_locked()
        assert diary.find_entry_by_id(101).get_entry_id() == 101
        assert diary.number_of_entries() == 1

    def test_deleteEntry_entryIsDeleted(self):
        diary = Diary("name", "password")
        assert diary.number_of_entries() == 0
        diary.create_entry("name", "body")
        diary.unlock_diary("password")
        diary.deleteEntry(101)
        assert diary.number_of_entries() == 0

    def test_deleteEntry_entryIsDeletedWithCorrectPassword(self):
        diary = Diary("name", "password")
        diary.create_entry("name", "body")
        assert diary.is_locked()
        diary.unlock_diary("password")
        diary.deleteEntry(101)
        assert diary.number_of_entries() == 0

    def test_incorrectPasswordCannotDeleteEntry_EntrySizeRemainsTheSame(self):
        diary = Diary("name", "password")
        assert diary.number_of_entries() == 0
        diary.create_entry("name", "body")
        diary.unlock_diary("password")
        with pytest.raises(EntryNotFoundError):
            diary.deleteEntry(109)
        assert diary.number_of_entries() == 1

    def test_diaryCannotBeAccessedWithPassword(self):
        diary = Diary("name", "password")
        assert diary.number_of_entries() == 0
        diary.create_entry("name", "body")
        with pytest.raises(UnlockDiary):
            diary.deleteEntry(109)
        assert diary.number_of_entries() == 1

    def testDiariesCanAddDiary(self):
        diaries: Diaries = Diaries()

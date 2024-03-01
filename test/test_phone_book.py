from apps.test import phone_book
import unittest


class phone_book_test(unittest.TestCase):
    def test_that_i_can_save_contact(self):
        phone_book1 = phone_book.Phone_book()
        self.assertEqual("contact saved successfully", phone_book1.save_contact("biokes", "08112164332"))

    def test_numberSaved(self):
        phone_book_1 = phone_book.Phone_book()
        self.assertEqual("contact saved successfully", phone_book_1.save_contact("biokes", "08112164332"))
        self.assertEqual("contact deleted successfully", phone_book_1.delete_contact("biokes"))

    def test_if_number_is_deleted(self):
        phone_book_1 = phone_book.Phone_book()
        self.assertEqual("contact saved successfully", phone_book_1.save_contact("biokes", "08112164332"))
        self.assertEqual("contact deleted successfully", phone_book_1.delete_contact("biokes"))

    def testSavedNumberIsDeleted(self):
        phone_book_1 = phone_book.Phone_book()
        name_given = "Abbey"
        number_given = "09123456789"
        phone_book_1.save_contact(name_given, number_given)
        name_given = "Abbey1"
        number_given = "09123456789"
        phone_book_1.save_contact(name_given, number_given)
        self.assertEqual("contact deleted successfully", phone_book_1.delete_contact("Abbey1"))

    def test_that_deleted_numbers_are_not_found(self):
        phone_book_1 = phone_book.Phone_book()
        name_given = "Abbey1"
        number_given = "09123456789"
        phone_book_1.save_contact(name_given, number_given)
        self.assertEqual("contact deleted successfully", phone_book_1.delete_contact("Abbey1"))
        self.assertEqual("contact not found", phone_book_1.delete_contact("Abbey1"))

    def test_no_name_appears_before_saving_any(self):
        phone_book1 = phone_book.Phone_book()
        self.assertEqual("no contacts available.", phone_book1.display_contacts())

    def test_name_appears_after_saving(self):
        phone_book1 = phone_book.Phone_book()
        self.assertEqual("no contacts available.", phone_book1.display_contacts())
        phone_book1.save_contact("biokes", "09876543212")
        phone_book1.save_contact("Aiokes", "09876543212")
        phone_book1.save_contact("aiokes", "09876543212")
        self.assertEqual("Aiokes  ----------> 09876543212", phone_book1.search_by_name("Aiokes"))

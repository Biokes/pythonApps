import unittest
import phone_book

class MyTestCase(unittest.TestCase):
    def test_that_i_can_save_contact(self):
        phone_book1 = phone_book
        self.assertEqual("contact saved successfully",phone_book1.save_contact("biokes","08112164332"))







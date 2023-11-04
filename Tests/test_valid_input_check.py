import unittest
from Utils.valid_input_check import *


class TestEntryIsNumber(unittest.TestCase):

    def test_entry_field_is_number(self):
        self.assertEqual(entry_field_is_number(12), 12)
        self.assertEqual(entry_field_is_number(8938949303), 8938949303)
        self.assertEqual(entry_field_is_number("Hallo"), invalid_entry_return_value)
        self.assertEqual(entry_field_is_number("18F"), invalid_entry_return_value)

class TestEntryIsNotEmpty(unittest.TestCase):
    def test_entry_field_not_empty(self):
        self.assertEqual(entry_field_is_not_empty("hallo"), "hallo")
        self.assertEqual(entry_field_is_not_empty("1234"), "1234")
        self.assertEqual(entry_field_is_not_empty(""), invalid_entry_return_value)

class TestEntryIsEmail(unittest.TestCase):
    def test_entry_field_is_email(self):
        self.assertEqual(entry_field_is_email("hallo@hshs.nl"), "hallo@hshs.nl")
        self.assertEqual(entry_field_is_email("abcd@jeld.beje   "), "abcd@jeld.beje", "doesn't strip sting")
        self.assertEqual(entry_field_is_email("hsjewhd@nodot"), invalid_entry_return_value, "doesn't check for a dot")
        self.assertEqual(entry_field_is_email("noapenstaartje.nl"), invalid_entry_return_value, "Doesn't check for @")

class TestEntryIsZipcode(unittest.TestCase):
    def test_entry_field_is_zip(self):
        self.assertEqual(entry_field_is_zipcode("1234AB"), "1234AB", "correct zip code isn't recognized")
        self.assertEqual(entry_field_is_zipcode("1234 AB "), "1234AB", "correct zip code isn't recognized, doesn't strip spaces")
        self.assertEqual(entry_field_is_zipcode("AB3KL9"), invalid_entry_return_value, "Doesnt recognize invalid zip code")
        self.assertEqual(entry_field_is_zipcode("Kled90"), invalid_entry_return_value,"Doesnt recognize invalid zip code")

class TestEntryIsDate(unittest.TestCase):
    def test_entry_is_date(self):
        self.assertEqual(entry_is_date("11-11-2023"), "11-11-2023", "")


if __name__ == '__main__':
    unittest.main()

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
        self.assertEqual(entry_is_date("11-11-2024"), "11-11-2024", "correct date isn't recognized")
        self.assertEqual(entry_is_date("11/11/2024"), "11-11-2024", "function doesn't change '/' to '-'")
        self.assertEqual(entry_is_date("11/25/2023"), invalid_entry_return_value, "No error when invalid date is entered")

class TestBikeRentEntryIsNum(unittest.TestCase):
    def test_entry_bike_rent_is_num(self):
        self.assertEqual(entry_bike_rent_is_number(2), 2, "Doesn't recognize valid input")
        self.assertEqual(entry_bike_rent_is_number(""), 0, "Doesn't convert emptycell to zero")
        self.assertEqual(entry_bike_rent_is_number("hallo"), invalid_entry_return_value, "Doesn't return invalid_value when a string is enterd")

class TestBikeIsRented(unittest.TestCase):
    def test_bike_is_rented(self):
        self.assertEqual(bike_is_rented(1,0,0), 1, "Doesn't recognize when at least one bike is rented")
        self.assertEqual(bike_is_rented(0, 1, 0), 1, "Doesn't recognize when at least one bike is rented")
        self.assertEqual(bike_is_rented(0,0,1), 1, "Doesn't recognize when at least one bike is rented")
        self.assertEqual(bike_is_rented(1, 1, 1), 1, "Doesn't recognize when at least one bike is rented")
        self.assertEqual(bike_is_rented(0, 0, 0), 0, "Doesn't recognize when NO bike is rented")

if __name__ == '__main__':
    unittest.main()



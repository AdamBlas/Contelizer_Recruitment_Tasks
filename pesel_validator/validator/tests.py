from django.test import TestCase
from .validation import validate_pesel
from datetime import date

# Create your tests here.
class PeselValidationTests(TestCase):

    def test_valid_pesel_birthday_and_gender(self):
        test_cases = [
            ("44051401359", date(1944, 5, 14), "Male"),
            ("86112565349", date(1986, 11, 25), "Female"),
            ("76090649489", date(1976, 9, 6), "Female"),
            ("93042761347", date(1993, 4, 27), "Female"),
            ("05242183861", date(2005, 4, 21), "Female"),
            ("59101569873", date(1959, 10, 15), "Male"),
            ("89081362683", date(1989, 8, 13), "Female"),
            ("69032018726", date(1969, 3, 20), "Female"),
            ("98081544746", date(1998, 8, 15), "Female"),
        ]

        for pesel, birth_date, gender in test_cases:
                result = validate_pesel(pesel)
                self.assertTrue(result["is_valid"])
                self.assertEqual(result["birth_date"], birth_date)
                self.assertEqual(result["gender"], gender)

    def test_invalid_pesel_wrong_checksum(self):
        pesel_numbers = [ "44051401358",
                          "86112565348",
                          "76090649488",
                          "93042761348",
                          "05242183862",
                          "59101569874",
                          "89081362681",
                          "69032018727",
                          "44051401350",
                          "98081544745" ]

        for pesel in pesel_numbers:
            result = validate_pesel(pesel)
            self.assertFalse(result["is_valid"])
            self.assertEqual(result["reason"], "Control check failed")

    def test_invalid_pesel_not_digits(self):
        pesel_numbers = [ "4405140135a",
                          "861asds5348",
                          "           ",
                          "aaaaaaaaaaa",
                          "00000O00000",
                          "111111l1111",
                          "890813as681",
                          "690asddd727",
                          "440  aaa350",
                          "9808154474a" ]

        for pesel in pesel_numbers:
            result = validate_pesel(pesel)
            self.assertFalse(result["is_valid"])
            self.assertEqual(result["reason"], "PESEL must contain only digits")

    def test_invalid_pesel_wrong_length(self):
        pesel_numbers = [ "",
                          "2",
                          "488",
                          "761348",
                          "5242183",
                          "01159101569874",
                          "890254581362681",
                          "69038727",
                          "440523331401350",
                          "980815411700000045" ]

        for i in range(len(pesel_numbers)):
            with self.subTest(i=i):
                result = validate_pesel(pesel_numbers[i])
                self.assertFalse(result["is_valid"])
                self.assertEqual(result["reason"], "PESEL must have 11 digits")

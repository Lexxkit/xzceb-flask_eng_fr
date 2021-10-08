import unittest
from translator import english_to_french, french_to_english
from ibm_cloud_sdk_core import api_exception


class TestTranslator(unittest.TestCase):

    def test_english_to_french_success(self):
            
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_english_to_french_empty_input(self):

        with self.assertRaises(ValueError):
            self.assertEqual(english_to_french(None),None)

    def test_french_to_english_success(self):
            
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_french_to_english_empty_input(self):

        with self.assertRaises(ValueError):
            self.assertEqual(french_to_english(None),None)


if __name__ == '__main__':
    unittest.main()

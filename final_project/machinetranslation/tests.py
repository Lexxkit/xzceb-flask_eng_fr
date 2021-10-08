import unittest
from translator import englishToFrench, frenchToEnglish
from ibm_cloud_sdk_core import api_exception


class TestTranslator(unittest.TestCase):

    def test_english_to_french_success(self):
            
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def test_english_to_french_empty_input(self):

        self.assertRaises(api_exception.ApiException, englishToFrench, "")

    def test_french_to_english_success(self):
            
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

    def test_french_to_english_empty_input(self):

        self.assertRaises(api_exception.ApiException, frenchToEnglish, "")


if __name__ == '__main__':
    unittest.main()

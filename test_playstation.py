from selenium import webdriver
from unittest.mock import patch
import unittest

class TestPlaystation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.browser = webdriver.Chrome('/Users/alvinescobar/Downloads/chromedriver')

    def tearDown(self):
        print('tearDown\n')

    def test_playstation_title(self):

        browser = self.browser
        browser.get('https://playstation.com/en-us')
        self.assertIn("PlayStation", browser.title)
        print("Playstation was in the Title")




if __name__ == '__main__':
    unittest.main()

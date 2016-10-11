# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest		#Python library for testing
 
 
class NewVisitorTest(unittest.TestCase):
 
    def setUp(self):			#initializes the test. It opens the browser and it waits for 3 seconds if needs to (if the page is not loaded).
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
 
    def tearDown(self):		#runs after each test. It closes the browser.
        self.browser.quit()
 
    def test_it_worked(self):		#asserts that the title of the webpage has Welcome to Django in it.
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)
 
if __name__ == '__main__':
    unittest.main(warnings='ignore')	# if Python runs the file directly (not imported) it will execute the function unittest.main()
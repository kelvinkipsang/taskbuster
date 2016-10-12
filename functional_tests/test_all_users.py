# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest		#Python library for testing
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase  
 
 
class HomeNewVisitorTest(LiveServerTestCase):
 
    def setUp(self):			#initializes the test. It opens the browser and it waits for 3 seconds if needs to (if the page is not loaded).
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
 
    def tearDown(self):		#runs after each test. It closes the browser.
        self.browser.quit()
 	
 	def get_full_url(self, namespace):	# auxiliar function named get_full_url that takes namespace (identifier for a url)
        return self.live_server_url + reverse(namespace)	#self.live_server_url gives you the local host url #reverse gives you the relative url of a given namespace, here /

    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))	#tests that the home page title contains the word TaskBuster
        self.assertIn("TaskBuster", self.browser.title)
    
	def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"),"rgba(200, 50, 255, 1)")	# tests that the h1 text has the desired color

 
if __name__ == '__main__':
    unittest.main(warnings='ignore')	# if Python runs the file directly (not imported) it will execute the function unittest.main()
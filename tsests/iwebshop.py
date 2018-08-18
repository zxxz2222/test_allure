import unittest
from selenium import webdriver

class IWebShop(unittest.TestCase):
    driver = webdriver.Firefox()
    def setUp(self):
        url=''
        IWebShop.driver.get()

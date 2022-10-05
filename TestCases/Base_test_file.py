import time
import unittest
# --------------------------------------------------------------------------------------
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Src.Pages.Main_page_file import MainPageClass


class BaseClass(unittest.TestCase):
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
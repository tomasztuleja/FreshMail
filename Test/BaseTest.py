import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Config.TestData import TestData
from Locators.Locators import Locators
from Pages.LoginPage import LoginPage



class BaseTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH, options=chrome_options)
       # self.driver.maximize_window()
        self.driver.get(TestData.BASE_URL)


    # Log in is not in scope of testing. It is needed before every test case
    def log_in(self):
        self.homePage = LoginPage(self.driver)
        self.homePage.enter_text(Locators.LOGIN, TestData.LOGIN)
        self.homePage.enter_text(Locators.PASSWORD, TestData.PASSWORD)
        self.homePage.click(Locators.SUBMIT)


   # def tear_down(self):
       # self.driver.close()
       # self.driver.quit()

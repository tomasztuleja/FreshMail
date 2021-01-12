import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Config.TestData import TestData




class BaseTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()

        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--incognito')
        #chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH, options=chrome_options)
        self.driver.maximize_window()
        self.driver.get(TestData.BASE_URL)

    def tear_down(self):
        self.driver.close()
        self.driver.quit()

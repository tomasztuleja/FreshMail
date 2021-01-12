from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # click
    def click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click()

    # assert web element text and given text
    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # enter text
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

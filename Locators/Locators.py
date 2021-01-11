from selenium.webdriver.common.by import By


class Locators:
    # --- LoginPage Locators ---
    LOGIN = (By.NAME, "login[email]")
    PASSWORD = (By.NAME, "login[password]")
    SUBMIT = (By.ID, "submit-login")
    LOGIN_TITLE = (By.CLASS_NAME, "login-tittle")

    # --- HomePage Locators ---
    RECIPIENTS = (By.XPATH, "//ul[@class='nav main-menu']//li[6]")

    # --- Recipients Locators ---
    ADD_LIST = (By.PARTIAL_LINK_TEXT, "Dodaj Listę")
    RECIPIENTS_LIST = (By.CLASS_NAME, "clearfix hover-buttons")

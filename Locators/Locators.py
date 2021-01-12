from selenium.webdriver.common.by import By


class Locators:
    # --- LoginPage Locators ---
    LOGIN = (By.NAME, "login[email]")
    PASSWORD = (By.NAME, "login[password]")
    SUBMIT = (By.ID, "submit-login")
    LOGIN_TITLE = (By.CLASS_NAME, "login-tittle")

    # --- HomePage Locators ---
    RE_LOG = (By.PARTIAL_LINK_TEXT, "Wyloguj innych i zaloguj mnie")
    RECIPIENTS = (By.PARTIAL_LINK_TEXT, "Odbiorcy")


    # --- Recipients Locators ---
    ADD_LIST_BUTTON = (By.PARTIAL_LINK_TEXT, "Dodaj")
    ADD_USER = (By.CLASS_NAME, "btn btn-normal control-item app-btn-add-subscribers")
    RECIPIENTS_LIST = (By.CLASS_NAME, "clearfix hover-buttons")
    LIST_CREATOR_NAME = (By.XPATH, "//input[@name='name']")
    ADD_LIST_BUTTON_MODAL = (By.ID, "verifyCode")
    EMPTY_LIST_TEXT = (By.CLASS_NAME, "subtitle")
    #LIST_IN_LIST_TABLE = (By.CLASS_NAME, "clickable row-fluid")
    #TYPE_MANUALLY_FIELD_MODAL = (By.PARTIAL_LINK_TEXT, "Wpisz")
    #TEXT_AREA_MODAL = (By.TAG_NAME, "textarea")
    #IMPORT_BUTTON_MODAL = (By.PARTIAL_LINK_TEXT, "Importuj")
    #RECIPIENT_IN_LIST = (By.NAME, "name")


from Config.TestData import TestData
from Locators.Locators import Locators
from Pages.HompePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.Recipients import Recipients
from Test.BaseTest import BaseTest


class RecipientsListTest(BaseTest):

    def setUp(self):
        super().setUp()
        super()

    def test1_add_list(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enter_text(Locators.LOGIN, TestData.LOGIN)
        self.loginPage.enter_text(Locators.PASSWORD, TestData.PASSWORD)
        self.loginPage.click(Locators.SUBMIT)
        self.homePage = HomePage(self.loginPage.driver)

        def after_potential_relog(page):
            self.recipientsPage = Recipients(self.homePage.driver)
            self.recipientsPage.click(Locators.ADD_LIST_BUTTON)
            self.recipientsPage.enter_text(Locators.LIST_CREATOR_NAME, "testowa")
            self.recipientsPage.click(Locators.ADD_LIST_BUTTON_MODAL)
            self.recipientsPage.assert_element_text(Locators.EMPTY_LIST_TEXT, TestData.EMPTY_LIST)

        try:
            self.homePage = HomePage(self.loginPage.driver)
            self.homePage.click(Locators.RE_LOG)
            after_potential_relog(self.homePage.driver)


        except:
            self.homePage = HomePage(self.loginPage.driver)
            self.homePage.click(Locators.RECIPIENTS)
            after_potential_relog(self.homePage.driver)



        super().tear_down()

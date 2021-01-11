from Locators.Locators import Locators
from Pages.HompePage import HomePage
from Pages.Recipients import Recipients
from Test.BaseTest import BaseTest


class RecipientsTest(BaseTest):

    def setUp(self):
        super().setUp()
        super().log_in()

    def test1(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click(Locators.RECIPIENTS)

        self.recipients = Recipients(self.driver)
        self.recipients.click(Locators.RECIPIENTS_LIST)






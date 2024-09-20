from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_HEADER = By.XPATH, '//span[text()="Sign into your Target account"]'

    def verify_sign_in_form(self):
        self.verify_text(*self.SIGN_IN_HEADER, expected_text="Sign into your Target account")
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SignInPage(Page):
    TARGET_SIGN_IN_URL = "https://www.target.com/login"
    SIGN_IN_HEADER = By.XPATH, '//span[text()="Sign into your Target account"]'
    USER_EMAIL = 'ktibq74n@gudri.com'
    USER_PASSWORD = '*********'
    EMAIL_FIELD = By.ID, 'username'
    PASSWORD_FIELD = By.ID, 'password'
    SIGN_IN_BUTTON = By.ID, 'login'
    TERMS_AND_CONDITIONS_LINK = By.CSS_SELECTOR, '[aria-label*="terms & conditions"]'
    TERMS_AND_CONDITIONS_P_URL = "terms-conditions"

    def open_sign_in_page(self):
        self.driver.get(self.TARGET_SIGN_IN_URL)
        sleep(3)

    def enter_email(self):
        self.wait_for_element_to_appear(*self.EMAIL_FIELD)
        self.input_text(*self.EMAIL_FIELD, text=self.USER_EMAIL)

    def enter_password(self):
        self.input_text(*self.PASSWORD_FIELD, text=self.USER_PASSWORD)

    def click_sign_in_button_sign_in_form(self):
        self.click(*self.SIGN_IN_BUTTON)

    def click_target_tc_link(self):
        self.click(*self.TERMS_AND_CONDITIONS_LINK)

    def verify_sign_in_form(self):
        self.verify_text(*self.SIGN_IN_HEADER, expected_text="Sign into your Target account")

    def verify_sign_in_form_disappears(self):
        self.wait_for_element_to_disappear(*self.SIGN_IN_HEADER)

    def verify_tc_page_opened(self):
        self.verify_partial_url(self.TERMS_AND_CONDITIONS_P_URL)
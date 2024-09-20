from selenium.webdriver.common.by import By

from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = By.ID, 'search'
    SEARCH_BTN = By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']"
    CART_BTN = By.XPATH, "//*[@data-test='@web/CartIcon']"
    SIGN_IN_BTN = By.XPATH, '//span[text()="Sign in"]'

    def type_searchbar(self, product):
        self.input_text(*self.SEARCH_FIELD, text=product)

    def click_search_button(self):
        self.click(*self.SEARCH_BTN)

    def click_cart_button(self):
        self.click(*self.CART_BTN)

    def click_sing_in_button(self):
        self.click(*self.SIGN_IN_BTN)
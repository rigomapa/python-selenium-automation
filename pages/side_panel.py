from selenium.webdriver.common.by import By

from pages.base_page import Page


class SidePanel(Page):
    SIGN_IN_EXPAND_PNL = By.XPATH, '//a[@data-test="accountNav-signIn"]'
    PRODUCT_NAME_SIDE_PANEL = By.CSS_SELECTOR, "h4"
    ADD_TO_CART_SIDE_PNL = By.CSS_SELECTOR, '[data-test="orderPickupButton"][id*=addToCartButton]'
    VIEW_AND_CHECKOUT_BTN = By.CSS_SELECTOR, '[href="/cart"]'

    def click_sign_in_button(self):
        self.click(*self.SIGN_IN_EXPAND_PNL)

    def click_add_to_cart_button_side_panel(self):
        self.wait_for_element_to_appear(*self.PRODUCT_NAME_SIDE_PANEL)
        self.click(*self.ADD_TO_CART_SIDE_PNL)

    def click_view_cart_checkout_button(self):
        self.click(*self.VIEW_AND_CHECKOUT_BTN)
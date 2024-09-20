from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    EMPTY_CART_HEADER = By.XPATH, "//*[text()='Your cart is empty']"
    CART_ITEM = By.CSS_SELECTOR, '[data-test="cartItem"]'

    def verify_cart_empty(self):
        actual_result = self.driver.find_element(*self.EMPTY_CART_HEADER).text
        expected_result = "Your cart is empty"
        assert actual_result == expected_result, f"Expected '{expected_result}', got '{actual_result}'"

    def verify_cart_contains_item(self):
        actual_result = len(self.find_elements(*self.CART_ITEM))
        assert actual_result > 0, "Cart is empty"
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SearchResultsPage(Page):
    ITEM_NAME_RESULTS = By.XPATH, '//div[@data-test="resultsHeading"]'
    SEARCH_RESULTS = By.CSS_SELECTOR, '[data-test="@web/SlotRenderer"]'
    ADD_TO_CART_SEARCH = By.CSS_SELECTOR, '[id*=addToCartButton]'

    def verify_results(self, item):
        actual_result = self.driver.find_element(*self.ITEM_NAME_RESULTS).text
        assert item in actual_result, f"Item name '{item}' not found in search results."

    def click_add_to_cart_button_search(self):
        # self.wait_for_element_to_appear(*self.SEARCH_RESULTS)
        sleep(8)
        self.wait_to_be_clickable_click(*self.ADD_TO_CART_SEARCH)
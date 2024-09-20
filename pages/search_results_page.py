from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    ITEM_NAME_RESULTS = By.XPATH, '//div[@data-test="resultsHeading"]'

    def verify_results(self, item):
        actual_result = self.driver.find_element(*self.ITEM_NAME_RESULTS).text
        assert item in actual_result, f"Item name '{item}' not found in search results."
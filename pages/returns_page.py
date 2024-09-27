from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page
from pages.header import Header


class ReturnsPage(Page):
    RETURNS_URL = 'https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges'
    HELP_TOPICS_DD = By.CSS_SELECTOR, 'select[id*="ViewHelpTopics"]'
    HEADER_TXT = (By.XPATH, '//h2[contains(text(), "{SUBSTRING}")]')
    # RETURNS_HEADER = By.XPATH, '//h1[contains(text(), "Returns")]'
    # topic_header = By.XPATH, '//h2[contains(text(), "Orders & Purchases")]'

    def _get_locator(self, expected_header_text):
        return [self.HEADER_TXT[0], self.HEADER_TXT[1].replace('{SUBSTRING}', expected_header_text)]

    def open_returns_page(self):
        self.open(self.RETURNS_URL)

    def select_topic_from_dd(self, option):
        dd = self.find_element(*self.HELP_TOPICS_DD)
        select = Select(dd)
        select.select_by_value(option)

    # def verify_returns_page_opened(self):
    #     self.wait_for_element_to_appear(*self.RETURNS_HEADER)
    #
    # def verify_topic_page_opened(self):
    #     self.wait_for_element_to_appear(*self.topic_header)

    def verify_header(self, expected_header_text):
        header_locator = self._get_locator(expected_header_text)
        self.wait_for_element_to_appear(*header_locator)

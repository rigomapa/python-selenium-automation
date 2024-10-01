from selenium.webdriver.support import expected_conditions as EC
from selenium. webdriver.support.wait import WebDriverWait

from support.logger import logger

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        logger.info(f'Opening page {url}')
        self.driver.get(url)

    def scroll(self):
        logger.info(f'Scrolling page')
        self.driver.execute_script("window.scrollBy(0, 400)")

    def find_element(self, *locator):
        logger.info(f'searching for element by {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        logger.info(f'Searching for elements by {locator}')
        return self.driver.find_elements(*locator)

    def get_text(self, *locator):
        logger.info(f'Getting text from {locator}')
        return self.driver.find_element(*locator).text

    def click(self, *locator):
        logger.info(f'Clicking element by  {locator}')
        self.driver.find_element(*locator).click()

    def input_text(self, *locator, text):
        logger.info(f'Typing text into {locator}')
        self.driver.find_element(*locator).send_keys(text)

    def get_current_window(self):
        logger.info(f'Getting current window handle')
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        logger.info(f'Waiting for new window to open')
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        logger.info(f'Switching to new window')
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window_by_id(self, window_id):
        logger.info(f'Switching to window by {window_id}')
        self.driver.switch_to.window(window_id)

    def close(self):
        logger.info(f'Closing window')
        self.driver.close()

    def wait_to_be_clickable(self, *locator):
        logger.info(f'Waiting for element by {locator} to be clickable')
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} is not clickable'
        )

    def wait_to_be_clickable_click(self, *locator):
        logger.info(f'Waiting for element by {locator} to be clickable and clicking')
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} is not clickable'
        ).click()

    def wait_for_element_to_appear(self, *locator):
        logger.info(f'Waiting for element by {locator} to appear')
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} did not appear'
        )

    def wait_for_element_to_disappear(self, *locator):
        logger.info(f'Waiting for element by {locator} to disappear')
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by {locator} did not disappear'
        )

    def verify_text(self, *locator, expected_text):
        logger.info(f'Finding element by {locator} to verify text')
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f'"{expected_text}" does not match "{actual_text}"'

    def verify_partial_text(self, *locator, expected_text):
        logger.info(f'Finding element by {locator} to verify partial text')
        actual_text = self.find_element(*locator).text
        assert actual_text in expected_text, f'Partial text "{expected_text}" not found in "{actual_text}"'

    def verify_url(self, expected_url):
        logger.info(f'Getting current url')
        current_url = self.driver.current_url
        assert current_url == expected_url, f'"{current_url}" does not match "{expected_url}"'

    def verify_partial_url(self, partial_url):
        logger.info(f'Getting current url')
        current_url = self.driver.current_url
        assert partial_url in current_url, f'Partial URL "{partial_url}" not found in "{current_url}"'

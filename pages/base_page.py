from selenium.webdriver.support import expected_conditions as EC
from selenium. webdriver.support.wait import WebDriverWait


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_text(self, *locator):
        return self.driver.find_element(*locator).text

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, *locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def wait_to_be_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} is not clickable'
        )

    def wait_to_be_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} is not clickable'
        ).click()

    def wait_for_element_to_appear(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} did not appear'
        )

    def wait_for_element_to_disappear(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by {locator} did not disappear'
        )

    def verify_text(self, *locator, expected_text):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f'"{expected_text}" does not match "{actual_text}"'

    def verify_partial_text(self, *locator, expected_text):
        actual_text = self.find_element(*locator).text
        assert actual_text in expected_text, f'Partial text "{expected_text}" not found in "{actual_text}"'

    def verify_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f'"{current_url}" does not match "{expected_url}"'

    def verify_partial_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url in expected_url, f'Partial URL "{current_url}" not found in "{expected_url}"'

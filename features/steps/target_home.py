from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


TARGET_URL = "https://www.target.com/"
SEARCHBAR = By.ID, 'search'
SEARCH_BTN = By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']"
ITEM_NAME_RESULTS = By.XPATH, '//div[@data-test="resultsHeading"]'


@given("Open Target.com")
def open_target_com(context):
    context.driver.get(TARGET_URL)


@when("User searches for {item} in search bar")
def user_searches(context, item):
    context.driver.find_element(*SEARCHBAR).send_keys(item)


@when('User clicks search button')
def click_search_button(context):
    context.driver.find_element(*SEARCH_BTN).click()


@then("Search Results displays {item} name")
def check_item_name(context, item):
    actual_result = context.driver.find_element(*ITEM_NAME_RESULTS).text
    assert item in actual_result, f"Item name '{item}' not found in search results."
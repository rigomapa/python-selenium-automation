from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Target.com")
def open_target_com(context):
    context.driver.get("https://www.target.com/")
    sleep(3)


@when("User searches for {item} in search bar")
def user_searches(context, item):
    context.driver.find_element(By.ID, 'search').send_keys(item)
    sleep(3)


@when('User clicks search button')
def click_search_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(3)


@then("Search Results displays {item} name")
def check_item_name(context, item):
    actual_result = context.driver.find_element(By.XPATH, '//div[@data-test="resultsHeading"]').text
    assert item in actual_result, f"Item name '{item}' not found in search results."
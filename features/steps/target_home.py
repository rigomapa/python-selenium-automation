from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


TARGET_URL = "https://www.target.com/"
SEARCHBAR = By.ID, 'search'
SEARCH_BTN = By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']"
ITEM_NAME_RESULTS = By.XPATH, '//div[@data-test="resultsHeading"]'
ITEM_COMMON = By.CSS_SELECTOR, '[data-test="@web/site-top-of-funnel/ProductCardWrapper"]'
ITEM_IMG = By.CSS_SELECTOR, '[data-test="@web/ProductCard/ProductCardImage"]'
ITEM_NAME = By.CSS_SELECTOR, '[data-test="product-title"]'


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


@then("Verify every product has image and name")
def check_image_name(context):
    sleep(5)
    context.driver.execute_script("window.scrollBy(0, 3000)", "")
    all_products = context.driver.find_elements(*ITEM_COMMON)
    for product in all_products:
        product_img = context.driver.find_element(*ITEM_IMG)
        product_name = context.driver.find_element(*ITEM_NAME)
        # print(f'Product name: {product_name}, product image: {product_img}') # this line is for testing purposes only
        assert product_name and product_img, f"Product name and image not found in search results."

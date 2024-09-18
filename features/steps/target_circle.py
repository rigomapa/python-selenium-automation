from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


TARGET_CIRCLE_URL = 'https://www.target.com/circle'
BENEFIT_ELEMENTS = By.CSS_SELECTOR, 'h3.h-margin-b-tiny'


@when('User opens Target Circle page')
def open_target_circle(context):
    context.driver.get(TARGET_CIRCLE_URL)


@then('A total amount of {num} benefits elements are displayed')
def verify_num_elements(context, num):
    total_elements = len(context.driver.find_elements(*BENEFIT_ELEMENTS))
    assert total_elements == int(num), f"A total of {total_elements} was found."

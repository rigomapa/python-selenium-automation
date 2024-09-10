from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('User opens Target Circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')
    sleep(4)


@then('A total amount of {num} benefits elements are displayed')
def verify_num_elements(context, num):
    total_elements = len(context.driver.find_elements(By.CSS_SELECTOR, 'h3.h-margin-b-tiny'))
    assert total_elements == int(num), f"A total of {total_elements} was found."

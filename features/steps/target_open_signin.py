from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SIGN_IN_BTN = By.XPATH, '//span[text()="Sign in"]'
SIGN_IN_EXPAND_PNL = By.XPATH, '//a[@data-test="accountNav-signIn"]'
SIGN_IN_HEADER = By.XPATH, '//span[text()="Sign into your Target account"]'


@when("User presses Sign In button")
def press_sign_in_button(context):
    context.driver.find_element(*SIGN_IN_BTN).click()


@when("User presses Sing In button on expanding panel")
def press_sign_in_button_ep(context):
    context.driver.find_element(*SIGN_IN_EXPAND_PNL).click()


@then("Sign in form page is displayed")
def sign_in_form_displayed(context):
    actual_result = context.driver.find_element(*SIGN_IN_HEADER).text
    expected_result = "Sign into your Target account"
    assert actual_result == expected_result, f"Expected: '{expected_result}', received: '{actual_result}'"
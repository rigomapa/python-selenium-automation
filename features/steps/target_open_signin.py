from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("User presses Sign In button")
def press_sign_in_button(context):
    context.driver.find_element(By.XPATH, '//span[text()="Sign in"]').click()
    sleep(3)


@when("User presses Sing In button on expanding panel")
def press_sign_in_button_ep(context):
    context.driver.find_element(By.XPATH, '//a[@data-test="accountNav-signIn"]').click()
    sleep(3)


@then("Sign in form page is displayed")
def sign_in_form_displayed(context):
    actual_result = context.driver.find_element(By.XPATH, '//span[text()="Sign into your Target account"]').text
    expected_result = "Sign into your Target account"
    assert actual_result == expected_result, f"Expected: '{expected_result}', received: '{actual_result}'"
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Target.com")
def open_target_com(context):
    context.driver.get("https://www.target.com/")
    sleep(5)


@when("User presses Cart button")
def press_cart(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/CartIcon']").click()
    sleep(5)


@then("Verify 'My Cart' window is displayed")
def verify_cart(context):
    actual_result = context.driver.find_element(By.XPATH, "//*[text()='Your cart is empty']").text
    expected_result = "Your cart is empty"
    assert actual_result == expected_result, f"Expected '{expected_result}', got '{actual_result}'"
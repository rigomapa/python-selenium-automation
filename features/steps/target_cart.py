from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("User presses Cart button")
def press_cart(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/CartIcon']").click()
    sleep(3)


@when('User clicks Add to cart button')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[id*=addToCartButton]').click()
    sleep(3)


@when('User clicks Add to cart button in side panel')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="orderPickupButton"][id*=addToCartButton]').click()
    sleep(3)


@when('User presses View cart & check out button')
def press_cart_checkout(context):
    context.driver.find_element(By.CSS_SELECTOR, '[href="/cart"]').click()
    sleep(3)


@then("Verify 'My Cart' window is displayed")
def verify_cart(context):
    actual_result = context.driver.find_element(By.XPATH, "//*[text()='Your cart is empty']").text
    expected_result = "Your cart is empty"
    assert actual_result == expected_result, f"Expected '{expected_result}', got '{actual_result}'"


@then('Cart screen contains item')
def verify_cart_contains(context):
    actual_result = len(context.driver.find_elements(By.CSS_SELECTOR, '[data-test="cartItem"]'))
    assert actual_result > 0, "Cart is empty"
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


CART_BTN = By.XPATH, "//*[@data-test='@web/CartIcon']"
SEARCH_RESULTS = By.CSS_SELECTOR, '[data-test="@web/SlotRenderer"]'
ADD_TO_CART_SEARCH = By.CSS_SELECTOR, '[id*=addToCartButton]'
ADD_TO_CART_SIDE_PNL = By.CSS_SELECTOR, '[data-test="orderPickupButton"][id*=addToCartButton]'
VIEW_AND_CHECKOUT_BTN = By.CSS_SELECTOR, '[href="/cart"]'
EMPTY_CART_HEADER = By.XPATH, "//*[text()='Your cart is empty']"
CART_ITEM = By.CSS_SELECTOR, '[data-test="cartItem"]'
PRODUCT_NAME_SIDE_PANEL = By.CSS_SELECTOR, "h4"


@when("User presses Cart button")
def press_cart(context):
    context.driver.find_element(*CART_BTN).click()


@when('User clicks Add to cart button')
def add_to_cart(context):
    context.driver.wait.until(EC.visibility_of_element_located((SEARCH_RESULTS)))
    context.driver.find_element(*ADD_TO_CART_SEARCH).click()


@when('User clicks Add to cart button in side panel')
def add_to_cart_side(context):
    context.driver.wait.until(EC.visibility_of_element_located((PRODUCT_NAME_SIDE_PANEL)))
    context.driver.find_element(*ADD_TO_CART_SIDE_PNL).click()


@when('User presses View cart & check out button')
def press_cart_checkout(context):
    context.driver.find_element(*VIEW_AND_CHECKOUT_BTN).click()


@then("Verify 'My Cart' window is displayed")
def verify_cart(context):
    actual_result = context.driver.find_element(*EMPTY_CART_HEADER).text
    expected_result = "Your cart is empty"
    assert actual_result == expected_result, f"Expected '{expected_result}', got '{actual_result}'"


@then('Cart screen contains item')
def verify_cart_contains(context):
    actual_result = len(context.driver.find_elements(*CART_ITEM))
    assert actual_result > 0, "Cart is empty"
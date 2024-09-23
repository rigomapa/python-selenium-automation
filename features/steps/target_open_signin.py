from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("open Sign In page")
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()


@when("User presses Sign In button")
def press_sign_in_button(context):
    context.app.header.click_sing_in_button()


@when("User presses Sing In button on expanding panel")
def press_sign_in_button_ep(context):
    context.app.side_panel.click_sign_in_button()


@when("User enters email address")
def enter_email(context):
    context.app.sign_in_page.enter_email()


@when("User enters password")
def enter_password(context):
    context.app.sign_in_page.enter_password()


@when("User presses Sing In button in Sign In form")
def press_sign_in_button_sign_in_page(context):
    context.app.sign_in_page.click_sign_in_button_sign_in_form()


@when("store original window")
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()


@when("click on target Terms and Conditions link")
def click_target_tc_link(context):
    context.app.sign_in_page.click_target_tc_link()


@when("switch to newly opened window")
def switch_to_new_window(context):
    context.app.sign_in_page.switch_to_new_window()


@then("Sign in form page is displayed")
def sign_in_form_displayed(context):
    context.app.sign_in_page.verify_sign_in_form()


@then("Verify Sign In form disappears")
def verify_sign_in_form_disappears(context):
    context.app.sign_in_page.verify_sign_in_form_disappears()


@then("verify Terms and Conditions page is opened")
def verify_tc_page_opened(context):
    context.app.sign_in_page.verify_tc_page_opened()


@then("user can close new window and switch back to original")
def close_tc_and_return(context):
    context.app.sign_in_page.close()
    context.app.sign_in_page.switch_to_window_by_id(context.original_window)
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@when("User presses Sign In button")
def press_sign_in_button(context):
    context.app.header.click_sing_in_button()


@when("User presses Sing In button on expanding panel")
def press_sign_in_button_ep(context):
    context.app.side_panel.click_sign_in_button()


@then("Sign in form page is displayed")
def sign_in_form_displayed(context):
    context.app.sign_in_page.verify_sign_in_form()
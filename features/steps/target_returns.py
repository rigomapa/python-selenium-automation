from selenium.webdriver.common.by import By
from behave import given, when, then


@given('user opens Returns and Exchanges page')
def open_returns_page(context):
    context.app.returns_page.open_returns_page()


@when('user selects topic {option} in Browse Help dropdown')
def select_topic_from_dd(context, option):
    context.app.returns_page.select_topic_from_dd(option)


# @then('verify Return and Exchanges page opens')
# def verify_returns_page_opened(context):
#     context.app.returns_page.verify_returns_page_opened()
#
#
# @then('Help Topic page is opened')
# def verify_topic_page(context):
#     context.app.returns_page.verify_topic_page_opened()

@then('verify {expected_header_text} page opens')
def verify_page_opened(context, expected_header_text):
    context.app.returns_page.verify_header(expected_header_text)
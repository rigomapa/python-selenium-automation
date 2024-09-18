from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


TARGET_HELP_URL = "https://help.target.com/help"
HELP_HEADER = By.CSS_SELECTOR, ".col-sm-12.bio .custom-h2"
SEARCH_BAR = By.CSS_SELECTOR, ".search-input"
SEARCH_BTN = By.CSS_SELECTOR, ".btn-sm.search-btn"
OPTION_BOXES = By.CSS_SELECTOR, ".box-column .grid_6"
MANAGE_MY_TARGET = By.CSS_SELECTOR, ".salesforceBox.txtAC.bigbox1"
CONTACT_RECALL_BOXES = By.CSS_SELECTOR, ".grid_4.boxSmallr.txtAC.bigbox2"


@given("User enters Target Help page")
def open_target_help(context):
    context.driver.get(TARGET_HELP_URL)


@then("Target Help header is present")
def verify_target_help_header(context):
    context.driver.find_element(*HELP_HEADER)


@then("Search bar is present")
def verify_search_bar(context):
    context.driver.find_element(*SEARCH_BAR)


@then("Search button is present")
def verify_search_button(context):
    context.driver.find_element(*SEARCH_BTN)


@then("There are {num} boxes under What would you like to do section")
def verify_num_box(context, num):
    actual_box_num = len(context.driver.find_elements(*OPTION_BOXES))
    assert actual_box_num == int(num), f"{actual_box_num} boxes were found"


@then("Manage my target box is present")
def verify_manage_box(context):
    context.driver.find_element(*MANAGE_MY_TARGET)


@then("Contact and recalls boxes are present")
def verify_contact_recalls(context):
    contact_recall_boxes = len(context.driver.find_elements(*CONTACT_RECALL_BOXES))
    assert contact_recall_boxes == 2, f"{contact_recall_boxes} boxes were found"
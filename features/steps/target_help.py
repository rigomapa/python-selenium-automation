from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("User enters Target Help page")
def open_target_help(context):
    context.driver.get("https://help.target.com/help")
    sleep(3)


@then("Target Help header is present")
def verify_target_help_header(context):
    context.driver.find_element(By.CSS_SELECTOR, ".col-sm-12.bio .custom-h2")


@then("Search bar is present")
def verify_search_bar(context):
    context.driver.find_element(By.CSS_SELECTOR, ".search-input" )


@then("Search button is present")
def verify_search_button(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-sm.search-btn")


@then("There are {num} boxes under What would you like to do section")
def verify_num_box(context, num):
    actual_num = len(context.driver.find_elements(By.CSS_SELECTOR, ".box-column .grid_6"))
    assert actual_num == int(num), f"{actual_num} boxes were found"


@then("Manage my target box is present")
def verify_manage_box(context):
    context.driver.find_element(By.CSS_SELECTOR, ".salesforceBox.txtAC.bigbox1")


@then("Contact and recalls boxes are present")
def verify_contact_recalls(context):
    bottom_boxes = len(context.driver.find_elements(By.CSS_SELECTOR, ".grid_4.boxSmallr.txtAC.bigbox2" ))
    assert bottom_boxes == 2, f"{bottom_boxes} boxes were found"
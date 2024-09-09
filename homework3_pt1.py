from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#path to chrome driver executable
driver_path = ChromeDriverManager().install()
#create a new chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open Amazon Sign in page (NOTE: the link bellow doesn't work):
driver.get("https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Fhomepage.html%2Fref%3Dnav_bb_ya%2F%3Fie%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

# Css locators:
driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")
driver.find_element(By.CSS_SELECTOR, "#ap_register_form .a-spacing-small")
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
driver.find_element(By.CSS_SELECTOR, "#ap_email")
driver.find_element(By.CSS_SELECTOR, "#ap_password")
driver.find_element(By.CSS_SELECTOR, "#ap_password_context_message_section .a-alert-content")
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")
driver.find_element(By.CSS_SELECTOR, "#continue")
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "[href*='signin']")




# sleep(5)
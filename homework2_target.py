from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# 1. Open link:
driver.get("https://www.target.com/")
# 2. Click Sing in button:
driver.find_element(By.XPATH, '//span[text()="Sign in"]').click()
# 3. Click Sign In panel:
driver.find_element(By.XPATH, '//a[@data-test="accountNav-signIn"]').click()
# 4.1 Verify Sign In page opened:
sleep(3)
actual_result = driver.find_element(By.XPATH, '//span[text()="Sign into your Target account"]').text
expected_result = "Sign into your Target account"

# if actual_result == expected_result:
#     print("Sign in page opened - Test Passed")
# else:
#     print(f"{actual_result} was not found, {expected_result} was found instead. - Test Failed")
assert actual_result == expected_result, f"Expected: '{expected_result}', received: '{actual_result}'"
print("'Sign into your Target account' text was found - Test Passed")

# 4.2 Verify Sign in button is present:
assert driver.find_element(By.ID, 'login'), f"Could not find 'Log In' button."
print("'Log In' button was found - Test Passed")

driver.quit()

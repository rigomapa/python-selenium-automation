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

# Test Case: search results page displays results from item entered at searchbar
driver.get("https://www.target.com/")
driver.find_element(By.ID, "search").send_keys("towel")
driver.find_element(By.XPATH, '//button[@data-test="@web/Search/SearchButton"]').click()
sleep(4)
actual_result = driver.find_element(By.XPATH, '//div[@data-test="resultsHeading"]')
assert "towel" in actual_result.text, f"Search key not found in search results.--Test Failed"
print("Search key was found in search results--Test passed")
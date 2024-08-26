from selenium import webdriver # imports webdriver
from selenium.webdriver.common.by import By # imports 'By'. Used to find locators
from selenium.webdriver.chrome.service import Service # Necessary to automate chrome
from webdriver_manager.chrome import ChromeDriverManager # Finds out chrome version. Necessary to automate chrome
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install() # installs the driver

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Generic code above

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('table')

# wait for 4 sec
sleep(4)

# click search button
driver.find_element(By.NAME, 'btnK').click()

# verify search results
assert 'table'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()

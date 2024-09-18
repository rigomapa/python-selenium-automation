from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then



PRODUCT_URL = "https://www.target.com/p/A-91511634"
COLOR_OPTIONS = By.CSS_SELECTOR, 'img[height="64px"]'
COLOR_TEXT = By.XPATH, '//*[@data-test="@web/VariationComponent"]//*[contains(text(), "color")]/..'


@given("User opens {product} page with color options")
def open_product_url(context, product):
    context.driver.get(PRODUCT_URL)
    sleep(8)


@then("Verify user can click through all colors")
def click_through_colors(context):
    expected_colors = [
        'grey', 'black/gum', 'dark khaki', 'navy/tan', 'stone/grey',
        'white/gum', 'white/navy/red', 'white/sand/tan'
    ]
    actual_colors = []
    
    context.driver.execute_script("window.scrollBy(0, 400)")
    context.driver.wait.until(EC.element_to_be_clickable((COLOR_OPTIONS)))
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors:
        color.click()
        current_color = context.driver.find_element(*COLOR_TEXT).text
        verified_color = current_color.split("\n")[1]
        actual_colors.append(verified_color)

    assert actual_colors == expected_colors, f"Expected {expected_colors}, got {actual_colors}"
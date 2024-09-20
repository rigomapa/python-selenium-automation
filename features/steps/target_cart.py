from behave import given, when, then


@when("User presses Cart button")
def press_cart(context):
    context.app.header.click_cart_button()


@when('User clicks Add to cart button in results')
def add_to_cart(context):
    context.app.search_results_page.click_add_to_cart_button_search()


@when('User clicks Add to cart button in side panel')
def add_to_cart_side(context):
    context.app.side_panel.click_add_to_cart_button_side_panel()


@when('User presses View cart & check out button')
def press_cart_checkout(context):
    context.app.side_panel.click_view_cart_checkout_button()


@then("Verify 'Your cart is empty' is displayed")
def verify_cart(context):
    context.app.cart_page.verify_cart_empty()


@then('Cart screen contains item')
def verify_cart_contains(context):
    context.app.cart_page.verify_cart_contains_item()
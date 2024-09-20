from pages.base_page import Page
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.side_panel import SidePanel
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.side_panel = SidePanel(driver)
        self.sign_in_page = SignInPage(driver)

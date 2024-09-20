from features.steps.target_home import TARGET_URL
from pages.base_page import Page



class MainPage(Page):
    TARGET_URL = "https://www.target.com/"

    def open_main(self):
        self.open(TARGET_URL)


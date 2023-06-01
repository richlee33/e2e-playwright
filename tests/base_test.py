from playwright.sync_api import Page
from pages.login import LoginPage

class BaseTest():
    def setup_class(self):
        self.home = "https://www.saucedemo.com/"

    def go_home(self, page: Page):
        page.goto(self.home)

    def go_home_and_login_standard_user(self, page: Page):
        page.goto(self.home)
        login_page = LoginPage(page)
        login_page.login_valid_user("standard_user")

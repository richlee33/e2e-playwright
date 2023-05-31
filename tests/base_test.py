from playwright.sync_api import Page
from pages.login import LoginPage


home = "https://www.saucedemo.com/"

def go_home(page: Page):
    page.goto(home)

def go_home_and_login_standard_user(page: Page):
    page.goto(home)
    login_page = LoginPage(page)
    login_page.login_valid_user("standard_user")

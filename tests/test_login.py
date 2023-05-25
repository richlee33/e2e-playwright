import pytest
import re
from playwright.sync_api import Page, expect
from pages.login import LoginPage
from pages.inventory import InventoryPage


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    # Go to the starting url before each test.
    page.goto("https://www.saucedemo.com/")
    yield
    print("afterEach")

def test_pageload(page: Page):
    EXPECTED_LOGO_TEXT = "Swag Labs"

    login_page = LoginPage(page)
    assert login_page.get_logo_text() == EXPECTED_LOGO_TEXT, "Log In page content did not load properly"

def test_valid_user(page: Page):
    login_page = LoginPage(page)
    login_page.login_valid_user("standard_user")
    inventory_page = InventoryPage(page)
    expect(inventory_page.page).to_have_url(re.compile(inventory_page.get_expected_url()))

def test_invalid_user(page: Page):
    EXPECTED_INVALID_USER_TEXT = "Sorry, this user has been locked out."

    login_page = LoginPage(page)
    expect(login_page.login_with_invalid_user("locked_out_user")).to_contain_text(EXPECTED_INVALID_USER_TEXT)
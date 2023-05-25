import pytest
import re
from playwright.sync_api import Page, expect
from pages.login import LoginPage
from pages.inventory import InventoryPage
from pages.cart import CartPage

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    # Go to the starting url and log in before each test.
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login_valid_user("standard_user")
    yield
    print("afterEach")

def test_url(page: Page):
    inventory_page = InventoryPage(page)
    inventory_page.click_view_cart()

    cart_page = CartPage(page)
    expect(cart_page.page).to_have_url(re.compile(cart_page.get_expected_url()))

def test_cart_badge_2_items(page: Page):
    inventory_page = InventoryPage(page)
    inventory_page.add_cart_bike_light()
    inventory_page.add_cart_backpack()
    inventory_page.click_view_cart()

    cart_page = CartPage(page)
    cart_item_count = cart_page.get_shopping_cart_badge_value()
    assert cart_item_count == "2", "Shopping cart badge value incorrect."

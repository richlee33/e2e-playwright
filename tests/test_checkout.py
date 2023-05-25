import pytest
import re
from playwright.sync_api import Page, expect
from pages.login import LoginPage
from pages.inventory import InventoryPage
from pages.cart import CartPage
from pages.checkout_1 import Checkout1Page
from pages.checkout_2 import Checkout2Page
from pages.checkout_complete import CheckoutCompletePage

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    # Go to the starting url and log in before each test.
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login_valid_user("standard_user")
    yield
    print("afterEach")

def test_checkout_scenario_single_item(page: Page):
    inventory_page = InventoryPage(page)
    expect(inventory_page.page).to_have_url(re.compile(".*inventory"))

    inventory_page.add_cart_bike_light()
    inventory_page.click_view_cart()

    cart_page = CartPage(page)
    cart_page.click_checkout()

    checkout_1_page = Checkout1Page(page)
    expect(checkout_1_page.page).to_have_url(re.compile(".*checkout-step-one"))
    checkout_1_page.fill_checkout_info("john")
    checkout_1_page.click_continue()

    checkout_2_page = Checkout2Page(page)
    expect(checkout_2_page.page).to_have_url(re.compile(".*checkout-step-two"))
    checkout_2_page.click_finish_button()

    checkout_complete_page = CheckoutCompletePage(page)
    expect(checkout_complete_page.page).to_have_url(re.compile(".*checkout-complete"))
    expect(checkout_complete_page.COMPLETE_HEADER).to_contain_text('Thank you for your order!')


def test_checkout_scenario_continue_shopping(page: Page):
    inventory_page = InventoryPage(page)
    inventory_page.add_cart_bike_light()
    inventory_page.click_view_cart()

    cart_page = CartPage(page)
    cart_page.click_continue_shopping()

    inventory_page.add_cart_backpack()
    inventory_page.click_view_cart()

    cart_page.click_checkout()

    checkout_1_page = Checkout1Page(page)
    checkout_1_page.fill_checkout_info("mary")
    checkout_1_page.click_continue()

    checkout_2_page = Checkout2Page(page)
    checkout_2_page.click_finish_button()

    checkout_complete_page = CheckoutCompletePage(page)
    expect(checkout_complete_page.COMPLETE_HEADER).to_contain_text('Thank you for your order!')

import pytest
import re
from playwright.sync_api import Page, expect
from pages.login import LoginPage
from pages.inventory import InventoryPage

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
    cart_page = inventory_page.click_view_cart()

    checkout_1_page = cart_page.click_checkout()
    expect(checkout_1_page.page).to_have_url(re.compile(".*checkout-step-one"))

    checkout_1_page.fill_checkout_info("john")

    checkout_2_page = checkout_1_page.click_continue()
    expect(checkout_2_page.page).to_have_url(re.compile(".*checkout-step-two"))

    checkout_complete_page = checkout_2_page.click_finish_button()
    expect(checkout_complete_page.page).to_have_url(re.compile(".*checkout-complete"))

    expect(checkout_complete_page.COMPLETE_HEADER).to_contain_text('Thank you for your order!')


def test_checkout_scenario_continue_shopping(page: Page):
    inventory_page = InventoryPage(page)
    inventory_page.add_cart_bike_light()

    cart_page = inventory_page.click_view_cart()

    inventory_page = cart_page.click_continue_shopping()

    inventory_page.add_cart_backpack()

    cart_page = inventory_page.click_view_cart()

    checkout_1_page = cart_page.click_checkout()

    checkout_1_page.fill_checkout_info("mary")

    checkout_2_page = checkout_1_page.click_continue()

    checkout_complete_page = checkout_2_page.click_finish_button()

    expect(checkout_complete_page.COMPLETE_HEADER).to_contain_text('Thank you for your order!')

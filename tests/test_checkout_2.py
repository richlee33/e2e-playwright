import pytest
import re
from playwright.sync_api import Page, expect
from tests.base_test import BaseTest
from pages.inventory import InventoryPage
from pages.cart import CartPage
from pages.checkout_1 import Checkout1Page
from pages.checkout_2 import Checkout2Page


class TestCheckout2(BaseTest):
    @pytest.fixture(scope="function", autouse=True)
    def before_each_after_each(self, page: Page):
        self.go_home_and_login_standard_user(page)
        yield

    testcases_summary_total = [ ("bikelight", "backpack", "39.98"),
                                ("bolttshirt", "jacket", "65.98"),
                                ]

    @pytest.mark.parametrize("item_1, item_2, total", testcases_summary_total)
    def test_summary_total(self, page: Page, item_1, item_2, total):
        inventory_page = InventoryPage(page)
        inventory_page.add_cart(item_1)
        inventory_page.add_cart(item_2)
        inventory_page.click_view_cart()

        cart_page = CartPage(page)
        cart_page.click_checkout()

        checkout_1_page = Checkout1Page(page)
        checkout_1_page.fill_checkout_info("mary")
        checkout_1_page.click_continue()

        checkout_2_page = Checkout2Page(page)
        item_total = checkout_2_page.get_item_total()
        print(item_total)
        assert total in item_total

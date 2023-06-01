import pytest
import re
from playwright.sync_api import Page, expect
from tests.base_test import BaseTest
from pages.inventory import InventoryPage
from pages.cart import CartPage

class TestCart(BaseTest):

    @pytest.fixture(scope="function", autouse=True)
    def before_each_after_each (self, page: Page):
        self.go_home_and_login_standard_user(page)
        yield

    def test_url(self, page: Page):
        inventory_page = InventoryPage(page)
        inventory_page.click_view_cart()

        cart_page = CartPage(page)
        expect(cart_page.page).to_have_url(re.compile(cart_page.get_expected_url()))

    def test_cart_badge_2_items(self, page: Page):
        inventory_page = InventoryPage(page)
        inventory_page.add_cart_bike_light()
        inventory_page.add_cart_backpack()
        inventory_page.click_view_cart()

        cart_page = CartPage(page)
        cart_item_count = cart_page.get_shopping_cart_badge_value()
        assert cart_item_count == "2", "Shopping cart badge value incorrect."

import pages.checkout_1
import pages.inventory


class CartPage():
    def __init__(self, page):
        self.page = page
        self.EXPECTED_URL = ".*cart"
        self.SHOPPING_CART_BADGE = page.locator("[class='shopping_cart_badge']")
        self.CONTINUE_SHOPPING_BUTTON = page.locator("[data-test='continue-shopping']")
        self.CHECKOUT_BUTTON = page.get_by_role("button", name="checkout")

    def get_expected_url(self):
        return self.EXPECTED_URL

    def click_continue_shopping(self):
        self.CONTINUE_SHOPPING_BUTTON.click()
        return pages.inventory.InventoryPage(self.page)

    def click_checkout(self):
        self.CHECKOUT_BUTTON.click()
        return pages.checkout_1.Checkout1Page(self.page)

    def get_shopping_cart_badge_value(self):
        return self.SHOPPING_CART_BADGE.text_content()


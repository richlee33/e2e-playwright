import pages.inventory


class CheckoutCompletePage():
    def __init__(self, page):
        self.page = page
        self.EXPECTED_URL = ".*checkout-complete"
        self.COMPLETE_HEADER = page.locator("[class='complete-header']")
        self.BACK_HOME_BUTTON = page.get_by_role("button", name="back-to-products")

    def click_back_home_button(self):
        self.BACK_HOME_BUTTON.click()
        return pages.inventory.InventoryPage(self.page)
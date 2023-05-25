class InventoryPage():
    def __init__(self, page):
        self.page = page
        self.EXPECTED_URL = ".*inventory"
        self.CART = page.locator("[class='shopping_cart_link']")
        self.BIKELIGHT = page.locator("[data-test='add-to-cart-sauce-labs-bike-light']")
        self.BACKPACK = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")

    def get_expected_url(self):
        return self.EXPECTED_URL

    def add_cart_bike_light(self):
        self.BIKELIGHT.click()

    def add_cart_backpack(self):
        self.BACKPACK.click()

    def click_view_cart(self):
        self.CART.click()

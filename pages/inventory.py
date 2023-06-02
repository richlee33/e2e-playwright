class InventoryPage():
    def __init__(self, page):
        self.page = page
        self.EXPECTED_URL = ".*inventory"
        self.CART = page.locator("[class='shopping_cart_link']")
        self.BIKELIGHT = page.locator("[data-test='add-to-cart-sauce-labs-bike-light']")
        self.BACKPACK = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.BOLTTSHIRT = page.locator("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
        self.JACKET = page.locator("[data-test='add-to-cart-sauce-labs-fleece-jacket']")

    def get_expected_url(self):
        return self.EXPECTED_URL

    def add_cart(self, item):
        if hasattr(self, item.upper()):
            add_cart_locator = getattr(self, item.upper())
            add_cart_locator.click()
        else:
            raise ValueError("Tried to add item to cart that does not have a locator in the InventoryPage class")

    def click_view_cart(self):
        self.CART.click()

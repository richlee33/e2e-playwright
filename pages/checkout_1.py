from utils import users
import pages.checkout_2


class Checkout1Page():
    def __init__(self, page):
        self.page = page
        self.EXPECTED_URL = ".*checkout-step-one"
        self.FIRST_NAME_INPUT = page.locator("input[data-test='firstName']")
        self.LAST_NAME_INPUT = page.locator("input[data-test='lastName']")
        self.ZIP_INPUT = page.locator("input[data-test='postalCode']")
        self.CONTINUE_CHECKOUT_BUTTON = page.locator("input[data-test='continue']")
        self.CANCEL_BUTTON = page.get_by_role("button", name="cancel")

    def enter_first_name(self, first_name):
        self.FIRST_NAME_INPUT.fill(first_name)

    def enter_last_name(self, last_name):
        self.LAST_NAME_INPUT.fill(last_name)

    def enter_zip(self, zip):
        self.ZIP_INPUT.fill(zip)

    def fill_checkout_info(self, name):
        checkout_user = users.get_checkout_info(name)
        self.enter_first_name(checkout_user["first_name"])
        self.enter_last_name(checkout_user["last_name"])
        self.enter_zip(checkout_user["zip"])

    def click_continue(self):
        self.CONTINUE_CHECKOUT_BUTTON.click()
        return pages.checkout_2.Checkout2Page(self.page)

    def click_cancel(self):
        self.CANCEL_BUTTON.click()
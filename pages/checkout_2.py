import pages.checkout_complete


class Checkout2Page():
    def __init__(self, page):
        self.page = page
        self.EXPECTED_URL = ".*checkout-step-two"
        self.CANCEL_BUTTON = page.get_by_role("button", name="cancel")
        self.FINISH_BUTTON = page.get_by_role("button", name="finish")

    def click_finish_button(self):
        self.FINISH_BUTTON.click()
        return pages.checkout_complete.CheckoutCompletePage(self.page)
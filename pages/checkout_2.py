class Checkout2Page():
    def __init__(self, page):
        self.page = page
        self.EXPECTED_URL = ".*checkout-step-two"
        self.CANCEL_BUTTON = page.get_by_role("button", name="cancel")
        self.FINISH_BUTTON = page.get_by_role("button", name="finish")
        self.ITEM_TOTAL =  page.locator("div[class='summary_subtotal_label']")

    def click_finish_button(self):
        self.FINISH_BUTTON.click()

    def get_item_total(self):
        return self.ITEM_TOTAL.text_content()

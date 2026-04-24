class CheckoutOverview:
    def __init__(self, page):
        self.page = page

        self.title = page.get_by_test_id("title")
        self.item_name = page.get_by_test_id("inventory-item-name")
        self.item_price = page.get_by_test_id("inventory-item-price")
        self.payment_info = page.get_by_test_id("payment-info-value")
        self.finish_button = page.get_by_test_id("finish")
        self.cancel_button = page.get_by_test_id("cancel")

    def get_product_name(self):
        return self.item_name.inner_text()

    def finish_checkout(self):
        print(f"Finishing order for: {self.get_product_name()}")

    def click_finish_checkout(self):
        self.finish_button.click()

    def click_cancel_checkout(self):
        self.cancel_button.click()

    

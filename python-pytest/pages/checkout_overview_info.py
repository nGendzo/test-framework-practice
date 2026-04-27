class CheckoutOverview:
    def __init__(self, page):
        self.page = page

        self.title = page.locator(".title")
        self.item_name = page.locator(".inventory_item_name")
        self.item_price = page.locator(".inventory-item-price")
        self.payment_info = page.locator(".summary_value_label")
        self.finish_button = page.locator("#finish")
        self.cancel_button = page.locator("#cancel")

    def get_product_name(self):
        return self.item_name.inner_text()

    def finish_checkout(self):
        print(f"Finishing order for: {self.get_product_name()}")

    def click_finish_checkout(self):
        self.finish_button.click()

    def click_cancel_checkout(self):
        self.cancel_button.click()

    

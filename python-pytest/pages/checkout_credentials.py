class CheckoutCredentials:
    def __init__(self, page):
        self.page = page
        self.first_name_input = page.get_by_test_id("first-name")
        self.last_name_input = page.get_by_test_id("last-name")
        self.postal_code_input = page.get_by_test_id("postal-code")
        self.continue_button = page.get_by_test_id("continue")
        self.cancel_button = page.get_by_test_id("cancel")

    def submit_checkout_info(self, first, last, zip_code):
        self.first_name_input.fill(first)
        self.last_name_input.fill(last)
        self.postal_code_input.fill(zip_code)
        self.continue_button.click()

    def cancel_checkout(self):
        self.cancel_button.click()
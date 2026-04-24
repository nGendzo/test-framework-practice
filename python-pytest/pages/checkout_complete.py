class CheckoutComplete:
    def __init__(self, page):
        self.page = page

        self.complete_header = page.get_by_test_id("complete-header")
        self.complete_text = page.get_by_test_id("complete-text")
        self.back_home_button = page.get_by_test_id("back-to-products")

    def get_success_message(self):
        return self.complete_header.inner_text()

    def go_back_home(self):
        self.back_home_button.click()
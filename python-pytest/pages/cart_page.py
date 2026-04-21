class CartPage:
    def __init__(self, page):
        self.page = page

        self.checkout_button = page.get_by_test_id("checkout")
        self.item_list_name = page.get_by_test_id("inventory-item-name")

    def open(self):
        self.page.goto("https://www.saucedemo.com/cart.html")

    def checkout(self):
        self.checkout_button.click();

class CartPage:
    def __init__(self, page):
        self.page = page

        self.checkout_button = page.locator("#checkout")
        self.item_list_name = page.get_by_test_id("inventory-item-name")
        self.number_of_items = page.locator(".cart_item")

    def open(self):
        self.page.goto("https://www.saucedemo.com/cart.html")

    def checkout(self):
        self.checkout_button.click()

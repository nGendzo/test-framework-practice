class ProductPage:
    def __init__(self, page):
        self.page = page

        self.add_to_cart_button = page.get_by_test_id("add-to-cart")
        self.cart_page_button = page.get_by_test_id("shopping-cart-link")
        self.burger_menu_button = page.get_by_test_id("#react-burger-menu-btn")
        self.inventory_page_button = page.get_by_test_id("inventory-sidebar-link")

    def open(self, item_id):
        self.page.goto(f"https://www.saucedemo.com/inventory-item.html?id={item_id}")

    def add_to_cart(self):
        self.add_to_cart_button.click()
    
    def cart_page(self):
        self.cart_page_button.click()

    def burger_menu(self):
        self.burger_menu_button.click()

    def go_to_inventory(self):
        self.burger_menu_button.click()
        self.inventory_page_button.click()


    
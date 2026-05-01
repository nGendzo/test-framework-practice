from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_complete import CheckoutComplete
from pages.checkout_credentials import CheckoutCredentials
from pages.checkout_overview_info import CheckoutOverview


class App:
    def __init__(self, page):
        self.page = page
        self.login = LoginPage(page)
        self.inventory = InventoryPage(page)
        self.product = ProductPage(page)
        self.cart = CartPage(page)
        self.checkout_complete = CheckoutComplete(page)
        self.checkout_credentials = CheckoutCredentials(page)
        self.checkout_overview = CheckoutOverview(page)


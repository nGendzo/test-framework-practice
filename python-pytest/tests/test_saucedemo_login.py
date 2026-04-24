import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_complete import CheckoutComplete
from pages.checkout_credentials import CheckoutCredentials
from pages.checkout_overview_info import CheckoutOverview


@pytest.mark.smoke

def test_successful_login(page):
    """
    To verify user can log in with valid credentials and
    access inventory page
    """

    inventory_page = InventoryPage(page)
    login_page = LoginPage(page)
    
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    expect(inventory_page.title_text).to_have_text('Products')
    print("\nLogin is successfull, found the header 'Products' header! ")
    

    expect(inventory_page.inventory_items).to_have_count(6)

    count = inventory_page.get_items_count()
    print(f"Verified: Found {count} items.")



@pytest.mark.e2e

def test_checkout_flow(page):
    login_p = LoginPage(page)
    inventory_p = InventoryPage(page)
    product_p = ProductPage(page)
    cart_p = CartPage(page)
    checkout_info_p = CheckoutCredentials(page)
    overview_p = CheckoutOverview(page)
    complete_p = CheckoutComplete(page)


    login_p.navigate()
    login_p.login("standard_user", "secret_sauce")
    expect(inventory_p.title_text).to_have_text("Products")

    inventory_p.open_item("Sauce Labs Backpack") 
    
    product_p.add_to_cart()
    product_p.open_cart()

    cart_p.checkout()
    
    checkout_info_p.submit_checkout_info("Walter", "White", "12345")

    print(f"Verifying item: {overview_p.get_product_name()}")
    overview_p.finish_checkout()

    expect(complete_p.complete_header).to_have_text("Thank you for your order!")
    print("Test passed: Purchase completed successfully!")


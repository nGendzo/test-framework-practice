from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_successful_login(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)


    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    #This is Assertion to verify Inventory page opened successfully
    expect(inventory_page.title_text).to_have_text("Products")


    print(f"\n\nWe are on the {inventory_page.get_title()} page!")
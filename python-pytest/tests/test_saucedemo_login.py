import pytest
from playwright.sync_api import expect


@pytest.mark.smoke

def test_successful_login(logged_in_app):
    """
    To verify user can log in with valid credentials and
    access inventory page
    """
    app = logged_in_app


    expect(app.inventory.title_text).to_have_text('Products')
    print("\nLogin is successfull, found the header 'Products' header! ")
    

    expect(app.inventory.inventory_items).to_have_count(6)

    count = app.inventory.get_items_count()
    print(f"Verified: Found {count} items")



@pytest.mark.smoke

def test_logout(logged_in_app):
    """
    To verify user who is logged in the application
    can log out by clicking on Log out button
    """

    app = logged_in_app

    expect(app.inventory.title_text).to_have_text('Products')
    print("\nLogin is successfull, found the header 'Products' header! ")

    expect(app.inventory.inventory_items).to_have_count(6)

    count = app.inventory.get_items_count()
    print(f"Verified: Found {count} items")

    app.inventory.open_burger_menu()

    expected_options = ["All Items", "About", "Logout", "Reset App State"]
    expect(app.inventory.burger_menu_items).to_have_text(expected_options)

    count = app.inventory.get_burger_items_count()
    print(f"Verified: Found {count} items in burger menu list -", expected_options)

    app.inventory.logout()

    expect(app.login.login_page_title).to_have_text("Swag Labs")

    actual_text = app.login.login_page_title.inner_text()
    print(f"Login page title is correctly displayed as '{actual_text}'")


@pytest.mark.e2e

def test_checkout_flow(logged_in_app):
    """
    To verify user can log in with valid credentials and
    make a purchase on available products
    """
    app = logged_in_app

    expect(app.inventory.title_text).to_have_text("Products")

    #inventory_p.open_item("Sauce Labs Backpack") 
    app.product.open(3)

    app.product.add_to_cart()
    app.product.cart_page()

    app.cart.checkout()
    
    app.checkout_credentials.submit_checkout_info("Walter", "White", "12345")

    print(f"\nVerifying item: {app.checkout_overview.get_product_name()}")
    app.checkout_overview.finish_checkout()
    app.checkout_overview.click_finish_checkout()

    expect(app.checkout_complete.complete_header).to_have_text("Thank you for your order!")
    print("Test passed: Purchase completed successfully!")



@pytest.mark.parametrize("user, password, expected_outcome",[
    ("standard_user", "secret_sauce", None),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("problem_user", "secretsauce", "Epic sadface: Username and password do not match any user in this service"),
    ("new_user", "password123@", "Epic sadface: Username and password do not match any user in this service")
])
def test_login_multiple_credentials(app, user, password, expected_outcome):
    """
    Verify login with valid and invalid credentials
    """

    app.login.navigate()
    app.login.login(user, password)

    if expected_outcome == None:
        expect(app.inventory.title_text).to_have_text("Products")
        print("\nThe user logged in successfully!")
    else:
        expect(app.login.login_error_message).to_contain_text(expected_outcome)
        print(f"\nUser {user} is blocked to login with correct error {expected_outcome}")



@pytest.mark.regression
def test_adding_multiple_products(logged_in_app):
    """Verify user can select multiple items and ensure 
    they are present in cart"""

    app = logged_in_app

    for i in range(6):
        app.product.open(i)
        app.product.add_to_cart()
        app.product.go_back_to_products_page()

    app.product.cart_page()

    actual_count = app.cart.number_of_items.count()

    expect(app.cart.number_of_items).to_have_count(6)
    print(f"\nItem number is correct and is {actual_count}")


    
        

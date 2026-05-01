class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login_page_title = page.locator(".login_logo")
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_text("Login")
        self.login_error_message = page.locator("[data-test='error']")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self, user, pwd):
        self.username_input.fill(user)
        self.password_input.fill(pwd)
        self.login_button.click()
    
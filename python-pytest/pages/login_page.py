class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_text("Login")


    def navigate(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self, user, pwd):
        self.username_input.fill(user)
        self.page.wait_for_timeout(2000)

        self.password_input.fill(pwd)
        self.page.wait_for_timeout(2000)

        self.login_button.click()
        self.page.wait_for_timeout(5000)

    
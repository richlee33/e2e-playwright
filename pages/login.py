from utils import users


class LoginPage():
    def __init__(self, page):
        self.page = page
        self.LOGO = page.locator("div[class='login_logo']")
        self.USERNAME_INPUT = page.locator("input[data-test='username']")
        self.PASSWORD_INPUT = page.locator("input[data-test='password']")
        self.LOGIN_BUTTON = page.locator("input[data-test='login-button']")
        self.ERROR_MESSAGE = page.locator("h3[data-test='error']")

    def get_logo_text(self):
        return self.LOGO.text_content()

    def enter_username(self, username):
        self.USERNAME_INPUT.fill(username)

    def enter_password(self, password):
        self.PASSWORD_INPUT.fill(password)

    def click_login_button(self):
        self.LOGIN_BUTTON.click()

    def login(self, user):
        test_user = users.get_user(user)
        self.enter_username(test_user["username"])
        self.enter_password(test_user["password"])
        self.click_login_button()

    def login_valid_user(self, user):
        self.login(user)

    def login_with_invalid_user(self, user):
        self.login(user)
        return self.ERROR_MESSAGE
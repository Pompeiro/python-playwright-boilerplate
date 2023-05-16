from playwright.sync_api import Page

from src.pages.base import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.resource_path = ""
        self.username_field = self.page.get_by_test_id("username")
        self.password_field = self.page.get_by_test_id("password")
        self.login_button = self.page.get_by_test_id("login-button")

    def login(self, email: str, password: str) -> None:
        self.username_field.fill(email)
        self.password_field.fill(password)
        self.login_button.click()

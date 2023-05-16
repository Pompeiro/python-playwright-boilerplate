from playwright.sync_api import Page

from src.settings import settings


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_url = settings.base_url
        self.resource_path = "/"

    def combine_url(self) -> str:
        return self.base_url + self.resource_path

    def navigate(self) -> None:
        self.page.goto(self.combine_url())

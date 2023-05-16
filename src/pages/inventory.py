from playwright.sync_api import Page

from src.pages.base import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.resource_path = "/inventory.html"
        self.sort_dropdown = self.page.get_by_test_id("product_sort_container")

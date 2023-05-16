from playwright.sync_api import Page, expect

from src.models.user import User
from src.pages import InventoryPage, LoginPage


def test_user_should_login_using_valid_credentials(page: Page, standard_user: User):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    page.wait_for_load_state("load")
    login_page.login(email=standard_user.name, password=standard_user.password)

    expect(page).to_have_url(inventory_page.combine_url())
    expect(inventory_page.sort_dropdown).to_be_visible()

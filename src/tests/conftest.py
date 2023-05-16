import pytest
from playwright.sync_api import Playwright

from src.models.user import User
from src.settings import settings


@pytest.fixture()
def standard_user():
    return User(name=settings.standard_user_name, password=settings.master_password)


@pytest.fixture(autouse=True, scope="session")
def set_custom_test_id(playwright: Playwright) -> None:
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture(scope="session")
def browser_context_args() -> dict:
    return {"viewport": {"width": 1920, "height": 1080}}

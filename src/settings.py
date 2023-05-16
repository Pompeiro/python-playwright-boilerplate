from pydantic import BaseSettings


class Settings(BaseSettings):
    base_url: str
    allure_url: str
    security_user: str
    security_pass: str
    standard_user_name: str = "standard_user"
    master_password: str = "secret_sauce"


settings = Settings()  # type: ignore[call-arg]

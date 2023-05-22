from playwright.sync_api import Locator, expect


class TextElement:
    def __init__(
        self,
        locator: Locator,
        static_text: str = "",
        startswith_static_text: bool = True,
    ) -> None:
        self.locator = locator
        self.static_text = static_text
        self.startswith_static_text = startswith_static_text

    def verify(self, dynamic_text: str):
        if self.startswith_static_text:
            full_text = self.static_text + str(dynamic_text)
        else:
            full_text = str(dynamic_text) + self.static_text
        expect(self.locator).to_have_text(full_text)

    def verify_soft(self, dynamic_text: str):
        expect(self.locator).to_contain_text(self.static_text)
        expect(self.locator).to_contain_text(dynamic_text)

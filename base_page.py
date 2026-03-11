from playwright.sync_api import Page, expect


class BasePage:
    """Base class for all page objects. Contains shared utilities and common actions."""

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        """Navigate to a URL and wait for the page to load."""
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    def get_title(self) -> str:
        return self.page.title()

    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"reports/screenshots/{name}.png", full_page=True)

    def wait_for_element(self, selector: str, timeout: int = 10000):
        self.page.wait_for_selector(selector, timeout=timeout)

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

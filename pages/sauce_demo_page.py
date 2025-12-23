"""Page object for Sauce Demo (https://www.saucedemo.com)

Provides locators and reusable actions for logging in and verifying inventory.
"""

class SauceDemoPage:
    def __init__(self, page):
        self.page = page

        # Locators
        self.username_input = page.locator('#user-name')
        self.password_input = page.locator('#password')
        self.login_button = page.locator('#login-button')
        self.inventory_list = page.locator('.inventory_list')
        self.error_container = page.locator('[data-test="error"]')

    def navigate(self, url: str) -> None:
        """Navigate to the given URL."""
        self.page.goto(url)

    def login(self, username: str, password: str) -> None:
        """Fill the login form and submit."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def is_inventory_visible(self) -> bool:
        """Return True if inventory list is visible after login."""
        return self.inventory_list.is_visible()

    def get_error_text(self) -> str:
        """Return any login error text (empty string if none)."""
        try:
            return self.error_container.inner_text()
        except Exception:
            return ""

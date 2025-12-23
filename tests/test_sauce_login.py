import pytest
import allure

from pages.sauce_demo_page import SauceDemoPage
from config.test_data import TestData

def test_sauce_demo_login(page, url):
    """Login to Sauce Demo using standard_user / secret_sauce and verify inventory loads.

    Uses the SauceDemoPage page object and TestData constants. Adds Allure steps and
    attaches screenshots at key points.
    """
    sauce = SauceDemoPage(page)

    with allure.step("Navigate to Sauce Demo"):
        sauce.navigate(url('SAUCE_DEMO_URL'))

    with allure.step("Submit login form"):
        sauce.login(TestData.SAUCE_USERNAME, TestData.SAUCE_PASSWORD)

    with allure.step("Verify inventory is visible"):
        try:
            assert sauce.is_inventory_visible(), "Inventory list should be visible after successful login"
        except AssertionError:
            # Capture screenshot only on failure
            allure.attach(page.screenshot(), "Failure Screenshot", allure.attachment_type.PNG)
            raise

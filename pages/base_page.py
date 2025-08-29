from playwright.sync_api import Page, expect
from utils import ApiUtils

class LazyPayPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_signup_button = page.get_by_role("button", name="Signup/Login")
        self.mobile_input = page.get_by_test_id("mobile-input-field")
        self.products_menu = page.get_by_role("button", name="Products Expand")
        self.paylater_link =  page.get_by_test_id("Products-menu-list").get_by_test_id("PayLater")
        self.heading_paylater = page.get_by_role("heading", name="Shop Now. Pay Later.")
        self.proceed_button = page.get_by_test_id("proceed-button")
        self.confirm_button = page.get_by_test_id("confirm-otp")

    def navigate(self, url):
        self.page.goto(url)
        
    def click_login_signup(self):
        self.login_signup_button.click()
        
    def enter_mobile_number(self, number: str):
        self.mobile_input.fill(number)
        expect(self.mobile_input).to_have_value(number)
        self.proceed_button.click()

    def fetch_otp(self, mobile_number: str) -> str:
        """
        Fetch OTP using the ApiUtils class
        Args:
            mobile_number: The mobile number to fetch OTP for
        Returns:
            str: The OTP value
        """
        return ApiUtils.fetch_otp(mobile_number)

    def enter_otp(self, otp: str):
        # Assuming there are 6 input fields for OTP
        for i, digit in enumerate(otp):
            otp_input = self.page.get_by_test_id(f"input-group-{i}")
            otp_input.fill(digit)
        # Wait for all digits to be filled
        self.page.wait_for_timeout(1000)
        # Click the proceed button after OTP entry
        self.confirm_button.click()

    def navigate_to_paylater(self):
        self.products_menu.hover()
        self.paylater_link.click()
        
    def validate_paylater_heading(self):
        expect(self.heading_paylater).to_have_text("Shop Now. Pay Later.")

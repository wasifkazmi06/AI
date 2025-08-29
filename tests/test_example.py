import pytest
from pages.base_page import LazyPayPage
from config import test_data, urls

def test_lazypay_login(page):
    # Initialize the page object
    lazy_pay = LazyPayPage(page)
    
    # Navigate to LazyPay website
    lazy_pay.navigate(urls.LAZYPAY_BASE_URL)
    
    # Click on Sign up / Login button
    lazy_pay.click_login_signup()
    
    # Enter mobile number and click proceed
    lazy_pay.enter_mobile_number(test_data.TEST_MOBILE_NUMBER)
    
    # Fetch OTP from API
    otp = lazy_pay.fetch_otp(test_data.TEST_MOBILE_NUMBER)
    
    # Enter the OTP
    lazy_pay.enter_otp(otp)

def test_paylater_heading(page):
    # Initialize the page object
    lazy_pay = LazyPayPage(page)
    
    # Navigate to LazyPay website
    lazy_pay.navigate(urls.LAZYPAY_BASE_URL)
    
    # Navigate to PayLater section
    lazy_pay.navigate_to_paylater()
    
    # Validate the heading text
    lazy_pay.validate_paylater_heading()

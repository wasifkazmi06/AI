import pytest
import allure
from pages.base_page import LazyPayPage
from config import test_data, urls

@allure.epic('LazyPay Web Application')
@allure.feature('Authentication')
@allure.severity(allure.severity_level.BLOCKER)
@allure.title('User can login with OTP verification')
def test_lazypay_login(page):
    with allure.step("Initialize LazyPay page"):
        lazy_pay = LazyPayPage(page)
    
    with allure.step("Navigate to LazyPay website"):
        lazy_pay.navigate(urls.LAZYPAY_BASE_URL)
        allure.attach(page.screenshot(), "Homepage Screenshot", allure.attachment_type.PNG)
    
    with allure.step("Click on Sign up / Login button"):
        lazy_pay.click_login_signup()
        allure.attach(page.screenshot(), "Login Form Screenshot", allure.attachment_type.PNG)
    
    with allure.step(f"Enter mobile number: {test_data.TEST_MOBILE_NUMBER}"):
        lazy_pay.enter_mobile_number(test_data.TEST_MOBILE_NUMBER)
        allure.attach(page.screenshot(), "Mobile Number Entered", allure.attachment_type.PNG)
    
    with allure.step("Fetch OTP from API"):
        otp = lazy_pay.fetch_otp(test_data.TEST_MOBILE_NUMBER)
        allure.attach(str(otp), "OTP Value", allure.attachment_type.TEXT)
    
    with allure.step("Enter the OTP"):
        lazy_pay.enter_otp(otp)
        allure.attach(page.screenshot(), "OTP Entered", allure.attachment_type.PNG)

@allure.epic('LazyPay Web Application')
@allure.feature('PayLater')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('PayLater section displays correct heading')
def test_paylater_heading(page):
    with allure.step("Initialize LazyPay page"):
        lazy_pay = LazyPayPage(page)
    
    with allure.step("Navigate to LazyPay website"):
        lazy_pay.navigate(urls.LAZYPAY_BASE_URL)
        allure.attach(page.screenshot(), "Homepage Screenshot", allure.attachment_type.PNG)
    
    with allure.step("Navigate to PayLater section"):
        lazy_pay.navigate_to_paylater()
        allure.attach(page.screenshot(), "PayLater Section Screenshot", allure.attachment_type.PNG)
    
    with allure.step("Validate the heading text"):
        expected_heading = test_data.PAYLATER_HEADING
        lazy_pay.validate_paylater_heading()
        allure.attach(f"Expected heading: {expected_heading}", "Heading Validation", allure.attachment_type.TEXT)

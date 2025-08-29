"""
Configuration file for test data
"""

class TestData:
    # User Data
    TEST_MOBILE_NUMBER = "7057031852"
    TENANT_ID = "ec35b493"
    
    # Business Data
    TEST_BUSINESS_NAME = "test_1"
    
    # Test Timeouts
    DEFAULT_TIMEOUT = 30000  # 30 seconds
    ANIMATION_TIMEOUT = 1000  # 1 second
    
    # Expected Messages
    PAYLATER_HEADING = "Shop Now. Pay Later."
    
    # Test Users
    USERS = {
        'standard_user': {
            'mobile': '7057031852',
            'name': 'Test User'
        },
        'business_user': {
            'mobile': '9999999999',
            'business_name': 'test_1'
        }
    }

"""
Configuration file for test data
"""

class TestData:
    # UI Test Data
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

    # API Test Data
    class LibraryAPI:
        # Request Data
        ADD_BOOK = {
            "name": "AI Automation 101",
            "aisle": "227",
            "author": "John foe"
        }
        
        DELETE_BOOK = {
            "ID": "33b4e746-c652-4266-aab7-7c8a5f203eee228"
        }
        
        # Query Parameters
        AUTHOR_NAME = "Author101"
        BOOK_ID = "1647127e-b77f-4827-b986-592301ef7068228"
        
        # Expected Response Messages
        ADD_BOOK_SUCCESS = "successfully added"
        DELETE_BOOK_SUCCESS = "book is successfully deleted"
        BOOK_NOT_FOUND = "The book by requested bookid / author name does not exists!"
        
        # Response Fields
        RESPONSE_FIELDS = {
            'MSG': 'Msg',
            'MESSAGE': 'msg',
            'BOOK_NAME': 'book_name',
            'AUTHOR': 'author',
            'ID': 'ID'
        }

    # Sauce Demo credentials for UI tests
    SAUCE_USERNAME = "standard_user"
    SAUCE_PASSWORD = "secret_sauce"

    # Optionally expose the Sauce user as part of USERS map
    USERS['sauce_standard_user'] = {
        'username': SAUCE_USERNAME,
        'password': SAUCE_PASSWORD
    }

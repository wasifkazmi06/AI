"""
Configuration file for URLs and endpoints
"""

class UrlConfig:
    def __init__(self):
        # UI Base URLs
        self.LAZYPAY_BASE_URL = "https://sandbox-web.lazypay.in"
        self.API_BASE_URL = "http://user-registration-sbox.internal.los.payufin.io"
        
        # UI API Endpoints
        self.FETCH_OTP_ENDPOINT = f"{self.API_BASE_URL}/v0/user/fetchOtp"
        
        # Library API Base URL
        self.LIBRARY_API_BASE_URL = "http://216.10.245.166"
        
        # Library API Full URLs
        self.ADD_BOOK_URL = f"{self.LIBRARY_API_BASE_URL}/Library/Addbook.php"
        self.DELETE_BOOK_URL = f"{self.LIBRARY_API_BASE_URL}/Library/DeleteBook.php"
        self.GET_BOOK_URL = f"{self.LIBRARY_API_BASE_URL}/Library/GetBook.php"
    
    # Database Configuration
    DB_CONFIG = {
        'host': 'localhost',
        'database': 'database_1',
        'user': 'root',
        'password': 'root'
    }

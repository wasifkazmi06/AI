"""
Configuration file for URLs and endpoints
"""

class UrlConfig:
    # Base URLs
    LAZYPAY_BASE_URL = "https://sandbox-web.lazypay.in"
    API_BASE_URL = "http://user-registration-sbox.internal.los.payufin.io"
    
    # API Endpoints
    FETCH_OTP_ENDPOINT = f"{API_BASE_URL}/v0/user/fetchOtp"
    
    # Database Configuration
    DB_CONFIG = {
        'host': 'localhost',
        'database': 'database_1',
        'user': 'root',
        'password': 'root'
    }

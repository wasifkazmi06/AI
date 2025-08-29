import requests
import mysql.connector
from typing import Dict, Optional, List, Tuple
from mysql.connector import Error

from config import test_data, urls

class ApiUtils:
    @staticmethod
    def get_db_connection():
        """Create database connection"""
        try:
            connection = mysql.connector.connect(
                host= urls.DB_CONFIG['host'],
                database=urls.DB_CONFIG['database'],
                user=urls.DB_CONFIG['user'],
                password=urls.DB_CONFIG['password']
            )
            return connection
        except Error as e:
            raise Exception(f"Error connecting to MySQL database: {e}")
        
    @staticmethod
    def fetch_otp(mobile_number: str) -> str:
        """
        Fetch OTP from the LazyPay API
        Args:
            mobile_number: The mobile number to fetch OTP for
        Returns:
            str: The OTP value
        Raises:
            Exception: If the API call fails
        """
        url = "http://user-registration-sbox.internal.los.payufin.io/v0/user/fetchOtp"
        params = {
            "mobile": mobile_number,
            "tenantId": test_data.TENANT_ID
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json().get("otpValue")
        raise Exception(f"Failed to fetch OTP. Status code: {response.status_code}")
    
    @staticmethod
    def fetch_business_address(business_name: str) -> Optional[Dict]:
        """
        Fetch business address from the database
        Args:
            business_name: Name of the business to fetch address for
        Returns:
            Dict containing the business address details or None if not found
        Raises:
            Exception: If there's an error executing the query
        """
        query = """
        SELECT 
            ba.business_id,
            ba.street_address,
            ba.city,
            ba.state,
            ba.postal_code,
            ba.country,
            b.business_name
        FROM 
            business b
            JOIN business_address ba ON b.business_id = ba.business_id
        WHERE 
            b.business_name = %s
        """
        
        connection = None
        cursor = None
        try:
            connection = ApiUtils.get_db_connection()
            cursor = connection.cursor()
            cursor.execute(query, (business_name,))
            result = cursor.fetchone()
            
            if result:
                return {
                    'business_id': result[0],
                    'street_address': result[1],
                    'city': result[2],
                    'state': result[3],
                    'postal_code': result[4],
                    'country': result[5],
                    'business_name': result[6]
                }
            return None
            
        except Error as e:
            raise Exception(f"Error executing query: {e}")
            
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

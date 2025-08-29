"""
Utility module for making HTTP requests
"""
import requests
from typing import Dict, Optional, Any
import json
from requests.exceptions import RequestException

class HttpClient:
    @staticmethod
    def post(url: str, payload: Dict, headers: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Make a POST request
        Args:
            url: The endpoint URL
            payload: The request payload
            headers: Optional request headers
        Returns:
            Dict containing the response data
        Raises:
            Exception if request fails
        """
        try:
            default_headers = {'Content-Type': 'application/json'}
            if headers:
                default_headers.update(headers)
            
            response = requests.post(url, json=payload, headers=default_headers)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise Exception(f"POST request failed: {str(e)}")

    @staticmethod
    def get(url: str, params: Optional[Dict] = None, headers: Optional[Dict] = None, handle_404: bool = False) -> Dict[str, Any]:
        """
        Make a GET request
        Args:
            url: The endpoint URL
            params: Optional query parameters
            headers: Optional request headers
            handle_404: If True, don't raise exception for 404 responses
        Returns:
            Dict containing the response data and status code
        Raises:
            Exception if request fails (except 404 when handle_404=True)
        """
        try:
            default_headers = {'Content-Type': 'application/json'}
            if headers:
                default_headers.update(headers)
            
            response = requests.get(url, params=params, headers=default_headers)
            
            # Handle 404 specially if requested
            if handle_404 and response.status_code == 404:
                return {
                    'status_code': 404,
                    'msg': response.json().get('msg', 'Not Found'),
                }
            
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            if handle_404 and '404' in str(e):
                return {
                    'status_code': 404,
                    'msg': 'Not Found'
                }
            raise Exception(f"GET request failed: {str(e)}")

    @staticmethod
    def delete(url: str, payload: Optional[Dict] = None, headers: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Make a DELETE request
        Args:
            url: The endpoint URL
            payload: Optional request payload
            headers: Optional request headers
        Returns:
            Dict containing the response data
        Raises:
            Exception if request fails
        """
        try:
            default_headers = {'Content-Type': 'application/json'}
            if headers:
                default_headers.update(headers)
            
            response = requests.delete(url, json=payload, headers=default_headers)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise Exception(f"DELETE request failed: {str(e)}")

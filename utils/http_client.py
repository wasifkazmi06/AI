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
    def get(url: str, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Make a GET request
        Args:
            url: The endpoint URL
            params: Optional query parameters
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
            
            response = requests.get(url, params=params, headers=default_headers)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
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

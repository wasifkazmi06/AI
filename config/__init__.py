"""Configuration module for the test automation framework."""

from .urls import UrlConfig
from .test_data import TestData

__all__ = [
    'UrlConfig',
    'TestData'
]

# Create instances for easy access
urls = UrlConfig()
test_data = TestData()

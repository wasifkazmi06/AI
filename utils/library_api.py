"""
Library API service module
"""
from typing import Dict, Optional
from utils.http_client import HttpClient
from config import urls, test_data
import uuid

class LibraryAPI:
    def __init__(self):
        self.http_client = HttpClient()
        self.urls = urls.UrlConfig()
        self.test_data = test_data.TestData()

    def add_book(self, name: str, aisle: str, author: str) -> Dict:
        """
        Add a new book
        Args:
            name: Book name
            aisle: Book aisle number
            author: Author name
        Returns:
            API response
        """
        payload = {
            "name": name,
            "isbn": str(uuid.uuid4()),
            "aisle": aisle,
            "author": author
        }
        return self.http_client.post(self.urls.ADD_BOOK_URL, payload)

    def get_book_by_author(self, author_name: str) -> Dict:
        """
        Get books by author name
        Args:
            author_name: Name of the author
        Returns:
            API response
        """
        params = {"AuthorName": author_name}
        return self.http_client.get(self.urls.GET_BOOK_ENDPOINT, params=params)

    def get_book_by_id(self, book_id: str) -> Dict:
        """
        Get book by ID
        Args:
            book_id: ID of the book
        Returns:
            API response
        """
        params = {"ID": book_id}
        return self.http_client.get(self.urls.GET_BOOK_ENDPOINT, params=params)

    def delete_book(self, book_id: str) -> Dict:
        """
        Delete a book by ID
        Args:
            book_id: ID of the book to delete
        Returns:
            API response
        """
        payload = {"ID": book_id}
        return self.http_client.delete(self.urls.DELETE_BOOK_ENDPOINT, payload)
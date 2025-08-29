"""
Tests for Library API endpoints
"""
import pytest
import allure
from utils.library_api import LibraryAPI
from config import test_data

@pytest.fixture
def library_api():
    return LibraryAPI()

@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Book Management')
@allure.title('Add new book to the library')
def test_add_book_successful(library_api):
    """Test successful book addition"""
    with allure.step("Prepare test data"):
        book_data = test_data.LibraryAPI.ADD_BOOK
        allure.attach(str(book_data), 'Test Data', allure.attachment_type.JSON)
    
    with allure.step("Add book to library"):
        response = library_api.add_book(
            name=book_data['name'],
            aisle=book_data['aisle'],
            author=book_data['author']
        )
        allure.attach(str(response), 'API Response', allure.attachment_type.JSON)
    
    with allure.step("Verify response"):
        assert response.get('Msg') == test_data.LibraryAPI.ADD_BOOK_SUCCESS
        assert 'ID' in response
        allure.attach(
            f"Book ID: {response.get('ID')}\nMessage: {response.get('Msg')}", 
            'Verification Details', 
            allure.attachment_type.TEXT
        )
    return response['ID']

@allure.severity(allure.severity_level.NORMAL)
@allure.story('Book Management')
@allure.title('Get book details by ID')
def test_get_book_by_id_successful(library_api):
    """Test getting book details by ID"""
    with allure.step("Get book ID from test data"):
        book_id = test_data.LibraryAPI.BOOK_ID
        allure.attach(str(book_id), 'Book ID', allure.attachment_type.TEXT)
    
    with allure.step(f"Retrieve book with ID: {book_id}"):
        response = library_api.get_book_by_id(book_id)
        allure.attach(str(response), 'API Response', allure.attachment_type.JSON)
    
    with allure.step("Verify response structure"):
        assert len(response) > 0
        assert isinstance(response, list)
        allure.attach(
            f"Response Length: {len(response)}\nResponse Type: {type(response)}", 
            'Response Validation', 
            allure.attachment_type.TEXT
        )

@allure.severity(allure.severity_level.NORMAL)
@allure.story('Book Management')
@allure.title('Get books by author name')
def test_get_book_by_author_successful(library_api):
    """Test getting books by author name"""
    with allure.step("Get author name from test data"):
        author_name = test_data.LibraryAPI.AUTHOR_NAME
        allure.attach(str(author_name), 'Author Name', allure.attachment_type.TEXT)
    
    with allure.step(f"Search books by author: {author_name}"):
        response = library_api.get_book_by_author(author_name)
        allure.attach(str(response), 'API Response', allure.attachment_type.JSON)
    
    with allure.step("Verify response structure"):
        assert len(response) > 0
        assert isinstance(response, list)
        allure.attach(
            f"Number of books found: {len(response)}\n" +
            f"Sample book titles: {[book.get('book_name', 'N/A') for book in response[:3]]}", 
            'Books Found Summary', 
            allure.attachment_type.TEXT
        )

@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Book Management')
@allure.title('Delete book from library')
def test_delete_book_successful(library_api):
    """Test successful book deletion"""
    with allure.step("Add a test book"):
        book_data = test_data.LibraryAPI.ADD_BOOK
        add_response = library_api.add_book(
            name=book_data['name'],
            aisle=book_data['aisle'],
            author=book_data['author']
        )
        book_id = add_response['ID']
        allure.attach(str(add_response), 'Add Book Response', allure.attachment_type.TEXT)
    
    with allure.step(f"Delete book with ID: {book_id}"):
        delete_response = library_api.delete_book(book_id)
        allure.attach(str(delete_response), 'Delete Book Response', allure.attachment_type.TEXT)
        assert delete_response.get('msg') == test_data.LibraryAPI.DELETE_BOOK_SUCCESS
    
    with allure.step("Verify book is deleted"):
        verify_response = library_api.get_book_by_id(book_id, handle_404=True)
        allure.attach(str(verify_response), 'Verify Deletion Response', allure.attachment_type.TEXT)
        assert verify_response.get('status_code') == 404
        assert verify_response.get('msg') == test_data.LibraryAPI.BOOK_NOT_FOUND
    


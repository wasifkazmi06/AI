"""
Tests for Library API endpoints
"""
import pytest
from utils.library_api import LibraryAPI
from config import test_data

@pytest.fixture
def library_api():
    return LibraryAPI()

@pytest.fixture
def test_data_instance():
    return test_data.TestData()

def test_add_book_successful(library_api, test_data_instance):
    """Test successful book addition"""
    book_data = test_data_instance.LibraryAPI.ADD_BOOK
    response = library_api.add_book(
        name=book_data['name'],
        aisle=book_data['aisle'],
        author=book_data['author']
    )
    
    assert response.get('Msg') == test_data_instance.LibraryAPI.ADD_BOOK_SUCCESS
    assert 'ID' in response
    # Store book ID for cleanup
    return response['ID']

def test_get_book_by_id_successful(library_api):
    """Test getting book details by ID"""
    book_id = test_data.TestData.BOOK_DATA['test_ids']['existing_book_id']
    response = library_api.get_book_by_id(book_id)
    
    assert response[0]['book_name'] == test_data.TestData.BOOK_DATA['valid_book']['name']
    assert response[0]['author'] == test_data.TestData.BOOK_DATA['valid_book']['author']

def test_get_book_by_author_successful(library_api):
    """Test getting books by author name"""
    author_name = test_data.TestData.BOOK_DATA['author_search']['name']
    response = library_api.get_book_by_author(author_name)
    
    assert len(response) > 0
    assert all(book['author'] == author_name for book in response)

def test_delete_book_successful(library_api):
    """Test successful book deletion"""
    # First add a book
    book_id = test_add_book_successful(library_api, test_data.TestData.BOOK_DATA['valid_book'])
    
    # Then delete it
    response = library_api.delete_book(book_id)
    assert response['msg'] == test_data.TestData.RESPONSES['delete_success']
    
    # Verify book is deleted
    get_response = library_api.get_book_by_id(book_id)
    assert get_response['msg'] == test_data.TestData.RESPONSES['no_book']

# LazyPay Test Automation Framework

A Playwright-based test automation framework for LazyPay web application using Python and pytest.

## Project Structure
```
├── config/                 # Configuration files
│   ├── __init__.py        # Config module initialization
│   ├── urls.py            # URL configurations
│   └── test_data.py       # Test data and constants
├── pages/                  # Page Object Models
│   ├── __init__.py
│   └── base_page.py       # Base page with common elements
├── tests/                  # Test files
│   └── test_example.py    # Example test cases
├── utils/                  # Utility functions
│   ├── __init__.py
│   └── api_utils.py       # API and database utilities
├── conftest.py            # pytest configurations
└── requirements.txt       # Project dependencies
```

## Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/wasifkazmi06/AI.git
cd AI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:
```bash
playwright install
```

## Configuration

### URL Configuration
Update base URLs and endpoints in `config/urls.py`:
```python
LAZYPAY_BASE_URL = "https://sandbox-web.lazypay.in"
API_BASE_URL = "http://user-registration-sbox.internal.los.payufin.io"
```

### Test Data
Update test data in `config/test_data.py`:
```python
TEST_MOBILE_NUMBER = "your_test_number"
TENANT_ID = "your_tenant_id"
```

### Database Configuration
Update database credentials in `config/urls.py`:
```python
DB_CONFIG = {
    'host': 'your_host_name',
    'database': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password'
}
```

## Running Tests

### Run all tests:
```bash
pytest
```

### Run specific test file:
```bash
pytest tests/test_example.py
```

### Run tests with verbose output:
```bash
pytest -v
```

### Run tests in headed mode:
Tests run in headed mode by default. Configuration is in `conftest.py`.

## Framework Features

### Page Object Model
- Page objects are in the `pages` directory
- `base_page.py` contains common elements and actions
- Each page should inherit from BasePage

### API Utilities
- API calls are centralized in `utils/api_utils.py`
- Includes OTP fetching and business data retrieval
- Database operations are handled with proper connection management

### Configuration Management
- URL configurations in `config/urls.py`
- Test data in `config/test_data.py`
- Easy import through config module

### Test Structure
- Tests are organized in the `tests` directory
- Uses pytest fixtures for browser and page management
- Implements Page Object Model pattern

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Submit a pull request

## Maintenance

### Adding New Tests
1. Create page objects in `pages` directory
2. Add test data to `config/test_data.py`
3. Create test file in `tests` directory
4. Use existing utilities from `utils`

### Best Practices
- Use Page Object Model pattern
- Keep configurations in config files
- Handle cleanup in test fixtures
- Use type hints for better code quality

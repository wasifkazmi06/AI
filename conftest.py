import sys
import pathlib

# Ensure project root is on sys.path so imports like `pages.*` resolve when pytest
# imports test modules during collection. This is intentionally early in the file.
ROOT = pathlib.Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pytest
from playwright.sync_api import Page, expect, sync_playwright, Browser, BrowserContext
from typing import Generator
from config import urls as urls_config, test_data as test_data_config


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add command-line option to select which browser to run tests with.
    Accept both `--browser-name` (preferred) and `--browser_name` (alias) to
     plugins (for example pytest-playwright) provide that option already and
    defining it locally causes argparse conflicts.
    """
    parser.addoption(
        "--browser-name",
        "--browser_name",
        action="store",
        default="chromium",
        choices=["chromium", "firefox", "webkit", "chrome", "msedge"],
        help="Browser to run tests with: chromium, firefox, webkit, chrome, msedge",
    )


@pytest.fixture(scope="session")
def requested_browser_name(request) -> str:
    """Fixture to get the requested browser name from command-line options."""
    if hasattr(request, "param"):
        return request.param

    # Value as exposed by our option (may be the default)
    val = request.config.getoption("browser_name")

    return val


@pytest.fixture(scope="session")
def browser(requested_browser_name: str) -> Generator[Browser, None, None]:
    playwright = sync_playwright().start()

    # Small debug print to make it clear which browser was requested when
    # running tests. This helps troubleshooting CLI/fixture conflicts.
    print(f"[pytest] launching {requested_browser_name} browser for the session.")

    bname = (requested_browser_name or "chromium").lower()
    if bname in ("chromium", "chrome", "msedge"):
        # Use chromium engine; allow channel override for real Chrome/MSEdge
        # Run headless by default and don't slow down execution unless debugging.
        launch_kwargs = {"headless":False, "slow_mo": 500}
        if bname == "chrome":
            browser = playwright.chromium.launch(channel="chrome", **launch_kwargs)
        elif bname == "msedge":
            browser = playwright.chromium.launch(channel="msedge", **launch_kwargs)
        else:
            browser = playwright.chromium.launch(**launch_kwargs)
    elif bname == "firefox":
        browser = playwright.firefox.launch(headless=False, slow_mo=500)
    elif bname == "webkit":
        browser = playwright.webkit.launch(headless=False, slow_mo=500)
    else:
        playwright.stop()
        raise ValueError(f"Unsupported browser: {requested_browser_name}")

    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    context = browser.new_context(
        viewport={
            "width": 1020,
            "height": 720
        }
    )
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="session")
def url() -> callable:
    """Factory fixture returning a callable to fetch a URL by name.

    Usage in tests:
        def test_x(page, url):
            base = url('LAZYPAY_BASE_URL')

    The factory tries the attribute as given, then its uppercase variant.
    """
    def _get(name: str) -> str:
        # Use the imported urls_config directly which is an instance of UrlConfig
        if hasattr(urls_config, name):
            return getattr(urls_config, name)
        upper = name.upper()
        if hasattr(urls_config, upper):
            return getattr(urls_config, upper)
        raise AttributeError(f"URL '{name}' not found in UrlConfig")

    return _get


@pytest.fixture(scope="session")
def test_data_value() -> callable:
    """Factory fixture returning a callable to fetch a test-data value by name.

    This uses the `test_data_config` imported from `config` directly so we don't
    need to expose the TestData instance as a separate fixture. Usage in tests:

        def test_x(test_data_value):
            mobile = test_data_value('TEST_MOBILE_NUMBER')

    The factory tries the attribute as given, then its uppercase variant.
    """
    def _get(name: str):
        if hasattr(test_data_config, name):
            return getattr(test_data_config, name)
        upper = name.upper()
        if hasattr(test_data_config, upper):
            return getattr(test_data_config, upper)
        raise AttributeError(f"Test data '{name}' not found in TestData")

    return _get


# End of file
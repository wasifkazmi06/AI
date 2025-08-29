import pytest
from playwright.sync_api import Page, expect, sync_playwright, Browser, BrowserContext
from typing import Dict, Generator

@pytest.fixture(scope="session")
def browser() -> Generator[Browser, None, None]:
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
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

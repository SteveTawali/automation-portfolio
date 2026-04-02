# tests/conftest.py
import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def api_request(playwright: Playwright):
    """Creates a Playwright API request context"""
    request_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    yield request_context
    request_context.dispose()
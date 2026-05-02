# Project 4: Page Object Model
# Notice how CLEAN this looks compared to previous projects!
# The test only cares about WHAT to test — not HOW to find elements

import pytest
import json
import os
from playwright.sync_api import Page
from pages.login_page import LoginPage

class TestLoginPOM:

    @pytest.fixture
    def credentials(self):
        # Load credentials from the data directory
        data_path = os.path.join(os.path.dirname(__file__), "..", "data", "credentials.json")
        with open(data_path, "r") as f:
            return json.load(f)["user_credentials"]

    def test_successfull_login(self, page: Page, credentials):
        # Use the first set of valid credentials
        user = credentials[0]
        login_page = LoginPage(page)
        login_page.goto()

        login_page.login(user["userEmail"], user["userPassword"])

        # ASSERT
        login_page.verify_login_successful()

    def test_wrong_password(self, page: Page, credentials):
        """User enters wrong password"""
        user = credentials[0]
        # ARRANGE
        login_page = LoginPage(page)
        login_page.goto()

        # ACT
        login_page.login(user["userEmail"], "WrongPassword!")

        # ASSERT
        login_page.verify_login_failed()

    def test_wrong_username(self, page: Page, credentials):
        """User enters wrong username"""
        # ARRANGE
        login_page = LoginPage(page)
        login_page.goto()

        # ACT
        login_page.login("wronguser", "Password123")

        # ASSERT
        login_page.verify_login_failed()


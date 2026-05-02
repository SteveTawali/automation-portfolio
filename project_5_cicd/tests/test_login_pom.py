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
        # Project 5 uses same structure as Project 4
        data_path = os.path.join(os.path.dirname(__file__), "..", "data", "credentials.json")
        if not os.path.exists(data_path):
             # Fallback to project 4 data if project 5 doesn't have its own
             data_path = os.path.join(os.path.dirname(__file__), "..", "..", "project_4_pom", "data", "credentials.json")
             
        with open(data_path, "r") as f:
            return json.load(f)["user_credentials"]

    def test_successfull_login(self, page: Page, credentials):
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


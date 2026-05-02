# tests/test_login.py
# Project 1: Login Test Suite
# Site: https://practicetestautomation.com/practice-test-login/

import pytest
import json
import os
from playwright.sync_api import Page, expect


class TestLogin:

    login_url = "https://practicetestautomation.com/practice-test-login/"

    @pytest.fixture
    def login_data(self):
        # Load credentials from JSON
        data_path = os.path.join(os.path.dirname(__file__), "login_data.json")
        with open(data_path, "r") as f:
            return json.load(f)

    def test_successful_login(self, page: Page, login_data):
        user = login_data["valid_user"]
        page.goto(self.login_url)
        page.get_by_label("Username").fill(user["username"])
        page.get_by_label("Password").fill(user["password"])
        page.get_by_role("button", name="Submit").click()

        # ASSERT
        expect(page.get_by_text(
            "Congratulations student. You successfully logged in!")).to_be_visible()

    def test_wrong_password(self, page: Page, login_data):
        user = login_data["valid_user"]
        page.goto(self.login_url)
        page.get_by_label("Username").fill(user["username"])
        page.get_by_label("Password").fill("WrongPassword")
        page.get_by_role("button", name="Submit").click()

        # ASSERT
        expect(page.locator("#error")).to_contain_text(
            "Your password is invalid!")

    def test_wrong_username(self, page: Page, login_data):
        user = login_data["invalid_user"]
        page.goto(self.login_url)
        page.get_by_label("Username").fill(user["username"])
        page.get_by_label("Password").fill("Password123")
        page.get_by_role("button", name="Submit").click()

        expect(page.locator("#error")).to_contain_text(
            "Your username is invalid!")

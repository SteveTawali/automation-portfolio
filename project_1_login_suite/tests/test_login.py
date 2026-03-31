# tests/test_login.py
# Project 1: Login Test Suite
# Site: https://practicetestautomation.com/practice-test-login/
# Valid credentials → username: student | password: Password123

import pytest
from playwright.sync_api import Page, expect


class TestLogin:

    login_url = "https://practicetestautomation.com/practice-test-login/"

    def test_successful_login(self, page: Page):
        page.goto(self.login_url)
        page.get_by_label("Username").fill("student")
        page.get_by_label("Password").fill("Password123")
        page.get_by_role("button", name="Submit").click()

        # ASSERT
        expect(page.get_by_text(
            "Congratulations student. You successfully logged in!")).to_be_visible()

    def test_wrong_password(self, page: Page):
        page.goto(self.login_url)
        page.get_by_label("Username").fill("student")
        page.get_by_label("Password").fill("WrongPassword")
        page.get_by_role("button", name="Submit").click()

        # ASSERT
        expect(page.locator("#error")).to_contain_text(
            "Your password is invalid!")

    def test_wrong_username(self, page: Page):
        page.goto(self.login_url)
        page.get_by_label("Username").fill("wronguser")
        page.get_by_label("Password").fill("Password123")
        page.get_by_role("button", name="Submit").click()

        expect(page.locator("#error")).to_contain_text(
            "Your username is invalid!")

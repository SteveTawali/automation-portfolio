# Project 4: Page Object Model
# Notice how CLEAN this looks compared to previous projects!
# The test only cares about WHAT to test — not HOW to find elements

import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

class TestLoginPOM:

    def test_successfull_login(self,page: Page):

        login_page = LoginPage(page)
        login_page.goto()

        login_page.login("student", "Password123")

        # ASSERT
        login_page.verify_login_successful()

    def test_wrong_password(self, page: Page):
        """User enters wrong password"""
        # ARRANGE
        login_page = LoginPage(page)
        login_page.goto()

        # ACT
        login_page.login("student", "WrongPassword!")

        # ASSERT
        login_page.verify_login_failed()

    def test_wrong_username(self, page: Page):
        """User enters wrong username"""
        # ARRANGE
        login_page = LoginPage(page)
        login_page.goto()

        # ACT
        login_page.login("wronguser", "Password123")

        # ASSERT
        login_page.verify_login_failed()


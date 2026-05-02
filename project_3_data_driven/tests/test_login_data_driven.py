# Project 3: Data-Driven Login Tests
# Same test runs multiple times with different data!

import pytest
import json
import os
from playwright.sync_api import Page, expect

def load_test_data():
    data_path = os.path.join(os.path.dirname(__file__), "test_data.json")
    with open(data_path, "r") as f:
        return json.load(f)

@pytest.mark.parametrize("username, password, expected", load_test_data())
class TestDataDrivenLogin:

    login_url = "https://practicetestautomation.com/practice-test-login/"

    def test_login(self, page: Page, username, password, expected):
        page.goto(self.login_url)
        page.get_by_label("Username").fill(username)
        page.get_by_label("Password").fill(password)
        page.get_by_role("button", name="Submit").click()

        # ASSERT
        if expected == "success":
            expect(page).to_have_url(
                "https://practicetestautomation.com/logged-in-successfully/"
            )
            expect(page.get_by_text(
                "Congratulations", exact=False)).to_be_visible()
        else:
            expect(page.locator("#error")).to_be_visible()

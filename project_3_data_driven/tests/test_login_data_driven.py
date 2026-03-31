# Project 3: Data-Driven Login Tests
# Same test runs multiple times with different data!

import pytest
from playwright.sync_api import Page, expect

# @pytest.mark.parametrize runs the test once for EACH set of data
# Format: ("param1, param2", [(data1), (data2), (data3)])

@pytest.mark.parametrize("username, password, expected", [
    # (Username,      Password,       expected result)
    ("student",      "Password123",  "success"),   # valid user
    ("student",      "WrongPass",    "failure"),   # wrong password
    ("wronguser",    "Password123",  "failure"),   # wrong username
    ("",             "",             "failure"),   # empty credentials
])

class TestDataDrivenLogin:

    login_url = "https://practicetestautomation.com/practice-test-login/"

    def test_login(self,page: Page, username, password, expected):
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
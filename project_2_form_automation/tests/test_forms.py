# Project 2: Form Automation
# Site: https://demoqa.com/automation-practice-form

import pytest
import json
import os
from playwright.sync_api import Page, expect

class TestForms:
    form_url = "https://demoqa.com/automation-practice-form"

    @pytest.fixture
    def form_data(self):
        # Load the data from JSON
        data_path = os.path.join(os.path.dirname(__file__), "form_data.json")
        with open(data_path, "r") as f:
            return json.load(f)["student_info"]

    def test_fill_student_registration_form(self, page: Page, form_data):
        page.goto(self.form_url)
        page.get_by_placeholder("First Name").fill(form_data["first_name"])
        page.get_by_placeholder("Last Name").fill(form_data["last_name"])
        page.get_by_placeholder("name@example.com").fill(form_data["email"])
        page.get_by_label(form_data["gender"], exact=True).click()

        page.get_by_placeholder("Mobile Number").fill(form_data["mobile"])

        # CALENDAR PICKER
        dob = form_data["date_of_birth"]
        page.locator("#dateOfBirthInput").click()
        page.locator(".react-datepicker__month-select").select_option(dob["month"])
        page.locator(".react-datepicker__year-select").select_option(dob["year"])
        page.get_by_role("gridcell", name=dob["label"]).click()

        for subject in form_data["subjects"]:
            page.locator(".subjects-auto-complete__input").fill(subject)
            page.get_by_text(subject, exact=True).click()

        for hobby in form_data["hobbies"]:
            page.get_by_label(hobby).click()

        # Handle file path - making it absolute to be robust
        abs_image_path = os.path.abspath(form_data["profile_picture"])
        page.locator("#uploadPicture").set_input_files(abs_image_path)

        # ACT - Text area
        page.get_by_placeholder("Current Address").fill(form_data["address"])

        # SUBMIT
        page.get_by_role("button", name="Submit").click()

        # ASSERT
        expect(page.get_by_text("Thanks for submitting the form")).to_be_visible()

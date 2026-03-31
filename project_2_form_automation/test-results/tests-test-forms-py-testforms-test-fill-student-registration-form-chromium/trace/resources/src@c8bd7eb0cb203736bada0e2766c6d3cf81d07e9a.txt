# Project 2: Form Automation
# Site: https://demoqa.com/automation-practice-form

import pytest
from playwright.sync_api import Page, expect

class TestForms:
    form_url = "https://demoqa.com/automation-practice-form"

    def test_fill_student_registration_form(self,page: Page):
        page.goto(self.form_url)
        page.get_by_placeholder("First Name").fill("Steven")
        page.get_by_placeholder("Last Name").fill("Tawali")
        page.get_by_placeholder("name@example.com").fill("tawalitest2@gmail.com")
        page.get_by_label("Male", exact=True).click()

        page.get_by_placeholder("Mobile Number").fill("0701020405")

        #CALENDAR PICKER
        # CALENDAR PICKER
        page.get_by_role("gridcell", name="Choose Tuesday, December 25th, 2001").click
        

        page.locator(".subjects-auto-complete__input").fill("English")
        page.get_by_text("English", exact=True).click()
        page.get_by_label("Sports").click()
        page.get_by_label("Music").click()

        page.locator("#uploadPicture").set_input_files("tests/test_image.jpg")

        # ACT - Text area
        page.get_by_placeholder("Current Address").fill("123 Test Street, Kakamega")

        #SUBMIT
        page.get_by_role("button", name="Submit").click()


        # ASSERT
        expect(page.get_by_text("Thanks for submitting the form")).to_be_visible()

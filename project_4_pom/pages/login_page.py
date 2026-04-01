# This is the Page Object for the Login Page
# It knows everything ABOUT the page — locators and actions
# Tests just CALL these methods — they don't need to know the details

from playwright.sync_api import Page, expect

class LoginPage:

    url = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self,page: Page):

        # Store the page so all methods can use it
        self.page = page

        #Define Locators in One Place
        self.username_field = page.get_by_label("Username")
        self.password_field = page.get_by_label("Password")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.error_message = page.locator("#error")
        self.success_message = page.get_by_text("Congratulations", exact=False)

    
    def goto(self):
        """Navigate to the login page"""
        self.page.goto(self.url)

    
    def login(self, username, password):
        """Perform login with given credentials"""
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.submit_button.click()

    
    def verify_login_successful(self):
        """Verify user is logged in successfully"""
        expect(self.page).to_have_url(
            "https://practicetestautomation.com/logged-in-successfully/"
        )
        expect(self.success_message).to_be_visible()
    
    def verify_login_failed(self):
        """Verify login failed with error message"""
        expect(self.error_message).to_be_visible()
    


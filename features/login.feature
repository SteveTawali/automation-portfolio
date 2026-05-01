Feature: Login
  Tests related to login


  Scenario: Verify user is logged in successfully
    Given I am on the login page
    When I enter username "student" and password "Password123"
    And I click the Submit button
    Then I should see a successful login message
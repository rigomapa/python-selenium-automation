
Feature: Tests for sign in functionality
  # Enter feature description here

  Scenario: Sign In form page is displayed when logged out user selects Sign In
    Given Open Target.com
    When User presses Sign In button
    And User presses Sing In button on expanding panel
    Then Sign in form page is displayed

  Scenario: Sign In form disappears once user logs in
    Given Open Target.com
    When User presses Sign In button
    And User presses Sing In button on expanding panel
    And User enters email address
    And User enters Password
    And User presses Sing In button in Sign In form
    Then Verify Sign In form disappears

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

  Scenario: User can open and close Terms and Conditions from Sign In page
    # Given open Sign In page - Sign in URL not working
    Given Open Target.com
    When User presses Sign In button
    And User presses Sing In button on expanding panel
    And store original window
    And click on target Terms and Conditions link
    And switch to newly opened window
    Then verify Terms and Conditions page is opened
    And user can close new window and switch back to original

  Scenario: "We can't find your account" message is displayed when user enters incorrect credentials
    # Given open Sign In page - Sign in URL not working
    Given Open Target.com
    When User presses Sign In button
    And User presses Sing In button on expanding panel
    Then Sign in form page is displayed
    When user enters incorrect email address
    And user enters incorrect password
    And User presses Sing In button in Sign In form
    Then verify 'We can't find your account' message is shown
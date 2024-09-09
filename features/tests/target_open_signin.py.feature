# Created by Ricardo Gomez at 9/6/2024
Feature: Logged out user can navigate to sign in
  # Enter feature description here

  Scenario: sign in form page is displayed when logged out user selects Sign In
    Given Open Target.com
    When User presses Sign In button
    And User presses Sing In button on expanding panel
    Then Sign in form page is displayed
# Created by rgomez at 9/9/2024
Feature: Tests for Target Search functionality


  Scenario: Search results for user-entered item are provided in search result screen.
    Given Open Target.com
    When User searches for tea in search bar
    And User clicks search button
    Then Search Results displays tea name

  Scenario: Search results screen provides product name and image
    Given Open Target.com
    When User searches for tea in search bar
    And User clicks search button
    Then Verify every product has image and name
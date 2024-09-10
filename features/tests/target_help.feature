
Feature: Tests for Target's Help page


  Scenario: Verify 6 elements from hwk 4
    Given User enters Target Help page
    Then Target Help header is present
    And Search bar is present
    And Search button is present
    And There are 6 boxes under What would you like to do section
    And Manage my target box is present
    And Contact and recalls boxes are present


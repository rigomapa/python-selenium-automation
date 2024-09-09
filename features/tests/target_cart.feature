# Created by Ricardo Gomez at 9/6/2024
Feature: Tests cart button functionality
  # Enter feature description here

  Scenario: Cart screen is opened when cart button is selected
    Given Open Target.com
    When User presses Cart button
    Then Verify 'My Cart' window is displayed
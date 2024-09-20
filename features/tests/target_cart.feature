# Created by Ricardo Gomez at 9/6/2024
Feature: Tests for cart functionality
  # Enter feature description here

  Scenario: Cart screen is opened when cart button is selected
    Given Open Target.com
    When User presses Cart button
    Then Verify 'Your cart is empty' is displayed

  Scenario: User can add items to cart
    Given Open Target.com
    When User searches for tea in search bar
    And User clicks search button
    And User clicks Add to cart button in results
    And User clicks Add to cart button in side panel
    And User presses View cart & check out button
    Then Cart screen contains item
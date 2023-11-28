Feature: Test Scenarios for Search functionality

  Scenario: All target benefit boxes are present
    Given Open Target page
    When Search for your table
    And Click on target search icon
    And Add to cart
    Then Verify table is added to cart
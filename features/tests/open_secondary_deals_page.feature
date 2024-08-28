Feature: User can open the Secondary deals page and go through the pagination

  Scenario: Open secondary deals page and go through the pagination
    Given Open main page
    When Log in to the page
    When Click on Secondary option at the left side menu
    Then Verify the right page opens
    Then Go to the final page using the pagination button
    Then Go back to the first page using the pagination button
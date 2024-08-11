Feature: Lists

    Scenario: Creating a new list
        Given I have a board with no lists
        When I click on the "Add a list" button and enter a list name
        Then the new list should appear on the board

    Scenario: Deleting a list
        Given I have a list named "Old List"
        When I click on the list settings and delete the list
        Then the list should be removed from the board

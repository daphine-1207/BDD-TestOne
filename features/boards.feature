Feature: Boards

    Scenario: Creating a new board 
        Given I am logged in to Trello
        When I click "Create a board" button
        Then I should see a new board with a default list

    Scenario: Renaming a board 
        Given I have a board named "Todo"
        When I click on the board settings and rename it to "Done"
        Then the board should be renamed to "Done"

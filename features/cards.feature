Feature: Cards

    Scenario: Creating a new card
        Given I have a list named "To-Do"
        When I click on the "Add a card" button and enter a card name
        Then the new card should appear in the "To-Do" list

    Scenario: Moving a card to another list
        Given I have a card named "Task" in the "To-Do" list
        When I drag and drop the card to the "Done" list
        Then the card should be moved to the "Done" list

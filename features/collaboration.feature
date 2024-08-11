Feature: Collaboration

    Scenario: Inviting a team member
        Given I have a board named "Project"
        When I invite a team member to the board via email
        Then the team member should receive an invitation and be added to the board

    Scenario: Assigning a task to a team member
        Given I have a card named "Task" and a team member named "Ozzy"
        When I assign the task to Ozzy
        Then Ozzy should be notified and see the task assigned to them

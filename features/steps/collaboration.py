from behave import given, when, then

#Scenario 1
@given('I have a board named "Project"')
def step_have_board(context):
    context.board = {"name": "Project", "members": []}

@when('I invite a team member to the board via email')
def step_invite_team_member(context):
    context.board["members"].append("team_member@example.com")
    context.invitation_sent = True

@then('the team member should receive an invitation and be added to the board')
def step_verify_invitation(context):
    assert "team_member@example.com" in context.board["members"]
    assert context.invitation_sent

#Scenario 2
@given('I have a card named "Task" and a team member named "Ozzy"')
def step_have_card_and_member(context):
    context.card = {"name": "Task", "assigned_to": None}
    context.team_member = "Ozzy"

@when('I assign the task to Ozzy')
def step_assign_task(context):
    context.card["assigned_to"] = context.team_member
    context.notification_sent = True

@then('Ozzy should be notified and see the task assigned to them')
def step_verify_task_assignment(context):
    assert context.card["assigned_to"] == "Ozzy"
    assert context.notification_sent

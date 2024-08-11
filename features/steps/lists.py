from behave import given, when, then

#Scenario 1
@given('I have a board with no lists')
def step_given_no_lists(context):
    context.board = []

@when('I click on the "Add a list" button and enter a list name')
def step_when_add_list(context):
    context.board.append("New List")

@then('the new list should appear on the board')
def step_then_list_appears(context):
    assert "New List" in context.board

#Scenario 2
@given('I have a list named "Old List"')
def step_given_old_list(context):
    context.board = ["Old List"]

@when('I click on the list settings and delete the list')
def step_when_delete_list(context):
    context.board.remove("Old List")

@then('the list should be removed from the board')
def step_then_list_removed(context):
    assert "Old List" not in context.board

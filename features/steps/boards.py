from behave import given, when, then

#Scenario 1
@given('I am logged in to Trello')
def step_logged_in(context):
    context.logged_in = True

@when('I click "Create a board" button')
def step_create_board(context):
    if context.logged_in:
        context.board = {"name": "New Board", "lists": ["Default List"]}

@then('I should see a new board with a default list')
def step_verify_new_board(context):
    assert context.board["name"] == "New Board"
    assert "Default List" in context.board["lists"]

#Scenario 2
@given('I have a board named "Todo"')
def step_existing_board(context):
    context.board = {"name": "Todo"}

@when('I click on the board settings and rename it to "Done"')
def step_rename_board(context):
    context.board["name"] = "Done"

@then('the board should be renamed to "Done"')
def step_verify_renamed_board(context):
    assert context.board["name"] == "Done"

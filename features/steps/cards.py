from behave import given, when, then

#Scenario 1
@given('I have a list named "To-Do"')
def step_have_list(context):
    context.lists = {"To-Do": []}

@when('I click on the "Add a card" button and enter a card name')
def step_add_card(context):
    context.lists["To-Do"].append("New Card")

@then('the new card should appear in the "To-Do" list')
def step_verify_new_card(context):
    assert "New Card" in context.lists["To-Do"]

#Scenario 2
@given('I have a card named "Task" in the "To-Do" list')
def step_have_card_in_list(context):
    context.lists = {"To-Do": ["Task"], "Done": []}

@when('I drag and drop the card to the "Done" list')
def step_move_card(context):
    context.lists["To-Do"].remove("Task")
    context.lists["Done"].append("Task")

@then('the card should be moved to the "Done" list')
def step_verify_card_moved(context):
    assert "Task" in context.lists["Done"]
    assert "Task" not in context.lists["To-Do"]

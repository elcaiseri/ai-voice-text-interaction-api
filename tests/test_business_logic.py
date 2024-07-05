from app.business_logic import generate_response

def test_generate_response():
    assert generate_response("move", "") == "Sure, navigating to the adjust page for you."
    assert generate_response("receive", "") == "Please specify the quantity and location for the items you want to receive."
    assert generate_response("adjust", "") == "Sure, let's adjust the quantity."
    assert generate_response("dispose", "") == "Item disposed and quantity updated."
    assert generate_response("greeting", "") == "Hey, how can I assist you today?"
    assert generate_response("inquire_quantity", "") == "You have 500 items in location X."
    assert generate_response("unknown", "") == "I'm not sure how to help with that."
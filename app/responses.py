def generate_response_text(intent, text):
    if intent == "move":
        return "Sure, navigating to the adjust page for you."
    elif intent == "receive":
        return "Please specify the quantity and location for the items you want to receive."
    elif intent == "adjust":
        return "Sure, let's adjust the quantity."
    elif intent == "dispose":
        return "Item disposed and quantity updated."
    elif intent == "greeting":
        return "Hey, how can I assist you today?"
    elif intent == "inquire_quantity":
        return "You have 500 items in location X."
    else:
        return "I'm not sure how to help with that."
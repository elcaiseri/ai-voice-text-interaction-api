import spacy

# Load spaCy's English NLP model
nlp = spacy.load("en_core_web_sm")

def extract_intent(text):
    """
    Extract the intent from the given text using spaCy NLP.
    
    Args:
    - text (str): The input text from which to extract the intent.
    
    Returns:
    - str: The extracted intent.
    """
    doc = nlp(text.lower())
    
    # Simple intent extraction based on keywords
    if any(token.text == "move" for token in doc):
        return "move"
    elif any(token.text == "receive" for token in doc):
        return "receive"
    elif any(token.text == "adjust" for token in doc):
        return "adjust"
    elif any(token.text == "dispose" for token in doc):
        return "dispose"
    elif any(token.text in {"hi", "hello", "hey"} for token in doc):
        return "greeting"
    elif "how many" in text.lower() and "items" in text.lower() and "location" in text.lower():
        return "inquire_quantity"
    else:
        return "unknown"
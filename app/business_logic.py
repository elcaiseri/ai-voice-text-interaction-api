from app.responses import generate_response_text

def generate_response(intent, text):
    response_text = generate_response_text(intent, text)
    return response_text
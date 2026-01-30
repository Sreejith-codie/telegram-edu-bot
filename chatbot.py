def get_response(user_text):
    user_text = user_text.lower()

    if "ai" in user_text:
        return "Artificial Intelligence is the simulation of human intelligence."
    elif "python" in user_text:
        return "Python is a popular programming language."
    else:
        return "Sorry, I could not understand your question."
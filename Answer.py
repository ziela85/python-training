import json

def load_db():
    with open('answers.json') as f:
        return json.load(f)

    db = load_db()

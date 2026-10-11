import json

def save_tickets(tickets, filename):
    with open(filename, "w") as file:
        json.dump(tickets, file, indent=4)

def load_tickets(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON file")
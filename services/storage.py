import json
import os

# path to where all the data gets saved
DB_FILE = "data/database.json"


def load_data():
    # if the file doesn't exist yet, just return an empty list
    if not os.path.exists(DB_FILE):
        return []

    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Warning: could not read the database file, starting fresh.")
        return []


def save_data(data):
    try:
        with open(DB_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Error: could not save data - {e}")

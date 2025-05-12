import json
import os

# File path to JSON family tree
JSON_FILE = 'family_tree.json'


def load_family_data():
    """Load current family data or return an empty template."""
    try:
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"family": []}


def save_family_data(data):
    """Save updated data back to the JSON file."""
    with open(JSON_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def add_family_member_logic(data_dict):
    """
    Accepts a dictionary of member data, validates and formats it,
    then appends it to the family tree JSON file.
    Returns a (success, message) tuple.
    """
    first_name = data_dict.get("first_name", "").strip()
    last_name = data_dict.get("last_name", "").strip()
    suffix = data_dict.get("suffix", "").strip()
    alive_str = data_dict.get("alive", "Yes")
    father = data_dict.get("father", "").strip()
    mother = data_dict.get("mother", "").strip()
    year_of_birth = data_dict.get("year_of_birth", "").strip()

    if not first_name or not last_name:
        return False, "First and last name are required."

    if not year_of_birth.isdigit():
        return False, "Year of birth must be a numeric value."

    alive = True if alive_str == "Yes" else False
    full_name = f"{first_name} {last_name} {suffix}".strip()

    data = load_family_data()
    data["family"].append({
        "first_name": first_name,
        "last_name": last_name,
        "suffix": suffix,
        "alive": alive,
        "father": father,
        "mother": mother,
        "year_of_birth": int(year_of_birth),
        "full_name": full_name
    })
    save_family_data(data)

    return True, f"{full_name} added to the family tree!"


def generate_family_report():
    """Return a formatted string containing all family members."""
    data = load_family_data()
    if not data["family"]:
        return "No family members in the file."
    output = ""
    for person in data["family"]:
        output += (
            f"{person['full_name']}\n"
            f" - Born: {person.get('year_of_birth', '?')}\n"
            f" - Alive: {person['alive']}\n"
            f" - Father: {person['father']}\n"
            f" - Mother: {person['mother']}\n\n"
        )
    return output.strip()

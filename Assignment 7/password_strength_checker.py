import getpass
import math
import string
import os

# Constants for file paths
DICTIONARY_FILE = "./words.txt"
COMMON_PASSWORDS_FILE = "./common_phrases.txt"
RECENT_PASSWORDS_FILE = "./recent_passwords.txt"

# Character set categories
CHARACTER_SETS = {
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "digits": string.digits,
    "special": string.punctuation
}

def get_password_input():
    """Prompt user for password input securely (without echoing)"""
    try:
        password = input("Enter your password: ")
    except Exception as e:
        print(f"Error getting password: {e}")
        return None
    return password

def calculate_entropy(password):
    """Calculate the entropy of a given password."""
    if not password:
        return 0

    char_space = 0
    for category, chars in CHARACTER_SETS.items():
        if any(c in chars for c in password):
            char_space += len(chars)

    entropy = len(password) * math.log2(char_space)
    return entropy

def check_dictionary_attack(password, dictionary_file):
    """Check if the password exists in a dictionary file."""
    if not os.path.exists(dictionary_file):
        print(f"Dictionary file {dictionary_file} not found.")
        return False

    try:
        with open(dictionary_file, "r", encoding="utf-8") as file:
            dictionary_words = set(word.strip().lower() for word in file)
    except Exception as e:
        print(f"Error reading dictionary file: {e}")
        return False

    return password.lower() in dictionary_words

def check_common_passwords(password, common_passwords_file):
    """Check if the password is in a common password list."""
    if not os.path.exists(common_passwords_file):
        print(f"Common password file {common_passwords_file} not found.")
        return False

    try:
        with open(common_passwords_file, "r", encoding="utf-8") as file:
            common_passwords = set(line.strip() for line in file)
    except Exception as e:
        print(f"Error reading common password file: {e}")
        return False

    return password in common_passwords

def check_recent_passwords(password, recent_passwords_file):
    """Check if the password has been used recently."""
    if not os.path.exists(recent_passwords_file):
        return False

    try:
        with open(recent_passwords_file, "r", encoding="utf-8") as file:
            recent_passwords = set(line.strip() for line in file)
    except Exception as e:
        print(f"Error reading recent password file: {e}")
        return False

    return password in recent_passwords

def save_password(password, recent_passwords_file):
    """Save password to the recent passwords file."""
    try:
        with open(recent_passwords_file, "a", encoding="utf-8") as file:
            file.write(password + "\n")
    except Exception as e:
        print(f"Error writing to recent password file: {e}")

def main():
    password = get_password_input()
    if not password:
        print("No password entered. Exiting.")
        return

    entropy = calculate_entropy(password)
    print(f"Password Entropy: {entropy:.2f} bits")

    if check_dictionary_attack(password, DICTIONARY_FILE):
        print("Warning: Your password is a common dictionary word!")

    if check_common_passwords(password, COMMON_PASSWORDS_FILE):
        print("Warning: Your password is a commonly used password!")

    if check_recent_passwords(password, RECENT_PASSWORDS_FILE):
        print("Warning: You have used this password before!")

    save_password(password, RECENT_PASSWORDS_FILE)
    print("Password saved for future reference.")

# Run the program
if __name__ == "__main__":
    main()

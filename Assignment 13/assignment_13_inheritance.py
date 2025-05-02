"""
Assignment 13 - Inherited Class with New Method and Overridden Method
This script inherits from a previous class (Person) and demonstrates:
1. Inheritance
2. New method added
3. Method override
"""

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_contact_info(self):
        return f"{self.name} can be reached at {self.email}"


class EnhancedPerson(Person):
    def __init__(self, name, email, nickname):
        super().__init__(name, email)
        self.nickname = nickname

    def get_contact_info(self):
        # Overridden method with more detail
        return f"{self.name} (aka {self.nickname}) can be contacted at {self.email}"

    def send_greeting(self):
        # New method
        return f"Hello from {self.nickname}!"


if __name__ == '__main__':
    print("TESTING ENHANCEDPERSON CLASS\n")

    enhanced = EnhancedPerson("Eve", "eve@example.com", "Evie")
    print(enhanced.get_contact_info())
    print(enhanced.send_greeting())

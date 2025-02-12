"""
James Payne - CIS206

BMI Calculator v4
----------------------------------

This program calculates the BMI (Body Mass Index) of a user based on their weight in pounds 
and height in feet and inches. This version includes:
- Input validation and exception handling.
- A loop for continuous input until the user chooses to exit.
- A BMI table for height (58 to 76 inches) and weight (100 to 250 pounds).
- Improved function documentation.

----------------------------------
"""

# Constants for conversions
POUNDS_TO_KILOGRAMS = 0.453592
INCHES_TO_METERS = 0.0254

def get_valid_input(prompt: str, input_type: type, min_value=None):
    """
    Continuously prompt the user for valid input based on the required type and range.
    Allows the user to exit by entering 'q'.
    """
    while True:
        try:
            user_input = input(prompt)
            if user_input.lower() == 'q':
                print("Exiting program.")
                return None

            value = input_type(user_input)

            if min_value is not None and value < min_value:
                raise ValueError(f"Input must be greater than or equal to {min_value}.")
            
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again or enter 'q' to quit.")

def calculate_bmi(weight_pounds: float, height_inches: int) -> float:
    """
    Calculate and return the BMI given weight in pounds and height in inches.
    """
    weight_kg = weight_pounds * POUNDS_TO_KILOGRAMS
    height_m = height_inches * INCHES_TO_METERS
    return weight_kg / (height_m ** 2)

def bmi_category(bmi: float) -> str:
    """
    Determine the BMI category based on BMI value.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def bmi_table():
    """
    Print a BMI table displaying BMI values for weights from 100 to 250 pounds (10-pound increments)
    and heights from 58 to 76 inches (2-inch increments).
    """
    print("\nBMI Table (Weight in lbs vs. Height in inches)\n")
    print(f"{'Weight (lbs)':<12}", end="")
    
    for height in range(58, 77, 2):
        print(f"{height} in".rjust(8), end="")
    print()

    for weight in range(100, 260, 10):
        print(f"{weight:<12}", end="")
        for height in range(58, 77, 2):
            bmi = calculate_bmi(weight, height)
            print(f"{bmi:.1f}".rjust(8), end="")
        print()

def main():
    """
    Main function to interactively calculate BMI with user input validation and looping.
    """
    while True:
        print("\n--- BMI Calculator ---")
        print("Enter 'q' at any time to exit.")
        
        weight_pounds = get_valid_input("Enter your weight in pounds: ", float, 1)
        if weight_pounds is None:
            break

        height_feet = get_valid_input("Enter your height in feet: ", int, 1)
        if height_feet is None:
            break

        height_inches = get_valid_input("Enter additional height in inches: ", int, 0)
        if height_inches is None:
            break

        total_height_inches = (height_feet * 12) + height_inches
        bmi = calculate_bmi(weight_pounds, total_height_inches)
        category = bmi_category(bmi)

        print(f"\nYour BMI is {bmi:.2f}, which falls under the category: {category}.")

    print("\nThank you for using the BMI calculator!\n")
    bmi_table()

if __name__ == "__main__":
    main()

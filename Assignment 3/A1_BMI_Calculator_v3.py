"""
James Payne - CIS206

BMI Calculator v3
----------------------------------

This program calculates the BMI (Body Mass Index) of a user based on their weight in pounds 
and height in feet and inches. This version adds input validation, parameter validation, 
assertions, and exception handling.

----------------------------------
"""

# Constants for conversions
POUNDS_TO_KILOGRAMS = 0.453592
INCHES_TO_METERS = 0.0254

def get_user_input() -> tuple:
    """Get user input for weight in pounds and height in feet and inches with validation."""
    try:
        weight_pounds = float(input("Enter your weight in pounds: "))
        if weight_pounds <= 0:
            raise ValueError("Weight must be a positive number.")
        
        height_feet = int(input("Enter your height in feet: "))
        if height_feet <= 0:
            raise ValueError("Height (feet) must be a positive integer.")
        
        height_inches = int(input("Enter your height in inches: "))
        if not (0 <= height_inches < 12):
            raise ValueError("Height (inches) must be between 0 and 11.")
        
        return weight_pounds, height_feet, height_inches
    
    except ValueError as e:
        print(f"Invalid input: {e}")
        exit(1)

def convert_weight_to_kilograms(weight_pounds: float) -> float:
    """Convert weight from pounds to kilograms. Validates parameter."""
    if not isinstance(weight_pounds, (int, float)) or weight_pounds <= 0:
        raise ValueError("Weight must be a positive number.")
    return weight_pounds * POUNDS_TO_KILOGRAMS

def convert_height_to_meters(height_feet: int, height_inches: int) -> float:
    """Convert height from feet and inches to meters. Validates parameters."""
    if not isinstance(height_feet, int) or not isinstance(height_inches, int):
        raise TypeError("Height feet and inches must be integers.")
    if height_feet <= 0 or not (0 <= height_inches < 12):
        raise ValueError("Invalid height values. Feet must be positive, inches must be between 0-11.")
    
    total_inches = (height_feet * 12) + height_inches
    return total_inches * INCHES_TO_METERS

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI using weight in kilograms and height in meters. Validates parameters."""
    if not isinstance(weight_kg, (int, float)) or not isinstance(height_m, (int, float)):
        raise TypeError("Weight and height must be numbers.")
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive numbers.")
    
    return weight_kg / (height_m ** 2)

def display_bmi_results(bmi: float) -> None:
    """Display BMI and classification with assertion validation."""
    assert isinstance(bmi, (int, float)), "BMI must be a numeric value."
    assert bmi > 0, "BMI must be positive."

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25.0 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"Your BMI is: {bmi:.1f}")
    print(f"You are classified as: {category}")
    print("BMI Legend:")
    print("Underweight: BMI < 18.5")
    print("Normal weight: BMI 18.5 - 24.9")
    print("Overweight: BMI 25.0 - 29.9")
    print("Obese: BMI 30.0 and above")

def main() -> None:
    """Main function to run the BMI calculator with exception handling."""
    try:
        weight_pounds, height_feet, height_inches = get_user_input()
        weight_kg = convert_weight_to_kilograms(weight_pounds)
        height_m = convert_height_to_meters(height_feet, height_inches)
        bmi = calculate_bmi(weight_kg, height_m)
        display_bmi_results(bmi)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    main()

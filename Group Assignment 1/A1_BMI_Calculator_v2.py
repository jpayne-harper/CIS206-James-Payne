
"""
BMI Calculator v2
-----------------
This program calculates the BMI (Body Mass Index) of a user based on their weight in pounds 
and height in feet and inches. The program is modular and uses functions for input, conversions, 
calculation, and output. Constants are defined for unit conversions, and the program avoids global 
variables by using parameters and return values.
"""

# Constants for conversions
POUNDS_TO_KILOGRAMS = 0.453592
INCHES_TO_METERS = 0.0254

def get_user_input() -> tuple:
    """Get user input for weight in pounds and height in feet and inches."""
    weight_pounds = float(input("Enter your weight in pounds: "))
    height_feet = int(input("Enter your height in feet: "))
    height_inches = int(input("Enter your height in inches: "))
    return weight_pounds, height_feet, height_inches

def convert_weight_to_kilograms(weight_pounds: float) -> float:
    """Convert weight from pounds to kilograms."""
    return weight_pounds * POUNDS_TO_KILOGRAMS

def convert_height_to_meters(height_feet: int, height_inches: int) -> float:
    """Convert height from feet and inches to meters."""
    total_inches = (height_feet * 12) + height_inches
    return total_inches * INCHES_TO_METERS

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI using weight in kilograms and height in meters."""
    return weight_kg / (height_m ** 2)

def display_bmi_results(bmi: float) -> None:
    """Display BMI and classification based on BMI value."""
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
    """Main function to run the BMI calculator."""
    weight_pounds, height_feet, height_inches = get_user_input()
    weight_kg = convert_weight_to_kilograms(weight_pounds)
    height_m = convert_height_to_meters(height_feet, height_inches)
    bmi = calculate_bmi(weight_kg, height_m)
    display_bmi_results(bmi)

if __name__ == "__main__":
    main()

def calculate_bmi(weight_pounds: float, height_feet: int, height_inches: int) -> None:
    """
    Calculate and display BMI with a legend based on user inputs.
    
    Args:
    - weight_pounds (float): Weight in pounds.
    - height_feet (int): Height in feet.
    - height_inches (int): Height in inches.
    
    Returns:
    - None
    """
    # Convert weight to kilograms and height to meters
    weight_kg = weight_pounds * 0.453592
    total_height_inches = (height_feet * 12) + height_inches
    height_m = total_height_inches * 0.0254

    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25.0 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    # Print results
    print(f"Your BMI is: {bmi:.1f}")
    print(f"You are classified as: {category}")
    print("\nBMI Legend:")
    print("Underweight: BMI < 18.5")
    print("Normal weight: BMI 18.5 - 24.9")
    print("Overweight: BMI 25.0 - 29.9")
    print("Obese: BMI 30.0 and above")
    print("\nSources:")
    print("BMI categories are based on: https://en.wikipedia.org/wiki/Body_mass_index")
    print("Metric conversion values are from: http://www.mathsisfun.com/metric-imperial-conversion-charts.html")

# Example usage
if __name__ == "__main__":
    # Example input
    weight_pounds = 150
    height_feet = 6
    height_inches = 2

    calculate_bmi(weight_pounds, height_feet, height_inches)

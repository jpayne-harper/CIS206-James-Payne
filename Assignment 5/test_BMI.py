import unittest
from A5_BMI_Calculator_v4 import calculate_bmi, bmi_category, POUNDS_TO_KILOGRAMS, INCHES_TO_METERS


class TestBMICalculator(unittest.TestCase):

    def test_normal_weight_bmi(self):
        # Test case for someone 5'8" (68 inches) and 150 pounds
        bmi = calculate_bmi(150, 68)
        print(f"\nNormal weight test - Calculated BMI: {bmi:.1f}, Expected: 22.8")
        self.assertAlmostEqual(bmi, 22.8, places=1)
        print(f"BMI Category: {bmi_category(bmi)}, Expected: Normal weight")
        self.assertEqual(bmi_category(bmi), "Normal weight")

    def test_underweight_bmi(self):
        # Test case for someone 5'10" (70 inches) and 120 pounds
        bmi = calculate_bmi(120, 70)
        print(f"\nUnderweight test - Calculated BMI: {bmi:.1f}, Expected: 17.2")
        self.assertAlmostEqual(bmi, 17.2, places=1)
        print(f"BMI Category: {bmi_category(bmi)}, Expected: Underweight")
        self.assertEqual(bmi_category(bmi), "Underweight")

    def test_overweight_bmi(self):
        # Test case for someone 6'0" (72 inches) and 190 pounds
        bmi = calculate_bmi(190, 72)
        print(f"\nOverweight test - Calculated BMI: {bmi:.1f}, Expected: 25.8")
        self.assertAlmostEqual(bmi, 25.8, places=1)
        print(f"BMI Category: {bmi_category(bmi)}, Expected: Overweight")
        self.assertEqual(bmi_category(bmi), "Overweight")

    def test_obese_bmi(self):
        # Test case for someone 5'6" (66 inches) and 200 pounds
        bmi = calculate_bmi(200, 66)
        print(f"\nObese test - Calculated BMI: {bmi:.1f}, Expected: 32.3")
        self.assertAlmostEqual(bmi, 32.3, places=1)
        print(f"BMI Category: {bmi_category(bmi)}, Expected: Obese")
        self.assertEqual(bmi_category(bmi), "Obese")

    def test_edge_cases(self):
        # Test conversion constants and extreme values
        print(f"\nConversion constants test:")
        print(f"POUNDS_TO_KILOGRAMS: {POUNDS_TO_KILOGRAMS}, Expected: 0.453592")
        self.assertAlmostEqual(POUNDS_TO_KILOGRAMS * 1, 0.453592)
        print(f"INCHES_TO_METERS: {INCHES_TO_METERS}, Expected: 0.0254")
        self.assertAlmostEqual(INCHES_TO_METERS * 1, 0.0254)
        # Test very tall person with low weight
        bmi = calculate_bmi(130, 76)  # 6'4" and 130 pounds
        print(f"\nExtreme case test - Tall person with low weight:")
        print(f"BMI: {bmi:.1f}, Should be less than 18.5")
        self.assertLess(bmi, 18.5)  # Should be underweight

    def test_value_input(self):
        # Test case for someone 5'8" (68 inches) and 150 pounds
        bmi = calculate_bmi(-150, 68)
        print(f"\nNormal weight test - Calculated BMI: {bmi:.1f}, Expected: 22.8")
        self.assertAlmostEqual(bmi, 22.8, places=1)
        print(f"BMI Category: {bmi_category(bmi)}, Expected: Normal weight")
        self.assertEqual(bmi_category(bmi), "Normal weight")


if __name__ == '__main__':
    unittest.main()

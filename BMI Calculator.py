def calculate_bmi(weight, height):
    return weight/height**2

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal Weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"
    
def main():
    print("Welcome to the BMI Calculator. Please work in Meters and Kilograms.")

    weight = float(input("Please enter your weight in kilograms: "))
    height = float(input("Please enter your height in meters: "))
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    print(f"\nYour BMI is {bmi:.2f}")
    print(f"This is considered {category}")

if __name__ == "__main__":
    main()

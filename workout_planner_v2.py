%%writefile workout_planner.py

def calculate_bmi(weight, height_cm):
    if weight <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be positive numbers.")
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def recommend_workout(bmi):
    if bmi < 18.5:
        return "30 minutes of light exercise", "High-calorie diet"
    elif 18.5 <= bmi < 24.9:
        return "45 minutes of moderate exercise", "Balanced diet"
    elif 25 <= bmi < 29.9:
        return "60 minutes of cardio", "Low-carb diet"
    else:
        return "75 minutes of intense workout", "Strict low-fat diet"

def recommend_location(bmi):
    if bmi < 25:
        return "Home workout recommended"
    else:
        return "Gym workout recommended"

def main():
    try:
        weight_input = input("Enter your weight in kg: ").strip()
        height_input = input("Enter your height in cm: ").strip()

        if not weight_input or not height_input:
            raise ValueError("Weight and height cannot be empty.")

        weight = float(weight_input)
        height = float(height_input)

        bmi = calculate_bmi(weight, height)
        workout, diet = recommend_workout(bmi)
        location = recommend_location(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(f"Recommended Workout: {workout}")
        print(f"Diet Plan: {diet}")
        print(f"Workout Location: {location}")

    except ValueError as e:
        print("Invalid input:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
from workout_planner import main
main()


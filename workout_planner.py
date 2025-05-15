def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive numbers.")
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return round(bmi, 2)

def recommend_workout(bmi):
    if bmi < 18.5:
        return "30 minutes light exercise (Yoga/Walking)", "High-calorie balanced diet"
    elif 18.5 <= bmi < 25:
        return "45 minutes moderate workout", "Balanced diet with proteins"
    elif 25 <= bmi < 30:
        return "60 minutes cardio & strength training", "Low-carb diet"
    else:
        return "75 minutes intensive workout", "Very low-carb & low-fat diet"

def workout_location(bmi):
    if bmi < 25:
        return "Home workout recommended"
    else:
        return "Gym workout recommended"

def main():
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (cm): "))
        bmi = calculate_bmi(weight, height)
        workout, diet = recommend_workout(bmi)
        location = workout_location(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(f"Workout Duration: {workout}")
        print(f"Diet Plan: {diet}")
        print(f"Workout Location: {location}")

    except ValueError as ve:
        print("Invalid input:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()

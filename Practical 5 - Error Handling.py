import math


# Exercise 1: Handling ZeroDivisionError
def safe_divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by Zero.")
        return None


# Exercise 2: Handling ValueError
def calculate_square_root(number1):
    try:
        if number1 < 0:
            raise ValueError
        return math.sqrt(number1)
    except (ValueError, TypeError):git
        print("Invalid input! Please enter a positive integer or a float value.")
        return None


# Exercise 3: Handling Generic Exceptions
def complex_math_task(num):
    try:
        # Task requires dividing (num - 5)
        result = num / (num - 5)
        return result
    except Exception as e:
        print("An error occurred during calculation.")
        return None


# Test Demonstrations
if __name__ == "__main__":
    print("--- Exercise 1 Tests ---")
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")

    print("\n--- Exercise 2 Tests ---")
    print(f"Sqrt of 16: {calculate_square_root(16)}")
    print(f"Sqrt of -4: {calculate_square_root(-4)}")

    print("\n--- Exercise 3 Tests ---")
    print(f"Task with num=10: {complex_math_task(10)}")
    print(f"Task with num=5: {complex_math_task(5)}")
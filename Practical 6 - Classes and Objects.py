# PROBLEM 1: BUGGY CODE FIX USING super()


class Person:

    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num

    def Display(self):
        print(f"Name: {self.name}, ID: {self.id_num}")


class Emp(Person):

    def __init__(self, name, id_num):
        # Using super() to initialize attributes from parent class
        super().__init__(name, id_num)

    def Print(self):
        print("Emp class called")


# Object Creation and Testing
Emp_details = Emp("Mayank", 103)
Emp_details.Print()
Emp_details.Display()

# PROBLEM 2: ANAGRAM CHECK


def is_anagram(str1, str2):
    # Normalize by converting to lowercase and removing whitespace
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)


# Testing Problem 2
word1 = "listen"
word2 = "silent"
print(f"\nAre '{word1}' and '{word2}' anagrams? {is_anagram(word1, word2)}")

# PROBLEM 3: ARMSTRONG NUMBER CHECK


def is_armstrong(number):
    num_str = str(number)
    power = len(num_str)
    total_sum = sum(int(digit) ** power for digit in num_str)
    return total_sum == number


# Testing Problem 3
test_num = 153
print(f"Is {test_num} an Armstrong number? {is_armstrong(test_num)}")


# PROBLEM 4: CAR DEALERSHIP INVENTORY SYSTEM (CLASSES & OBJECTS)


class Vehicle:
    # Task-2: Default color for all vehicles
    color = "white"

    # Task-1: Attributes for max_speed and mileage
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    # Task-3: Method to assign seating capacity
    def set_seating_capacity(self, capacity):
        self.seating_capacity = capacity

    # Task-4: Method to display all properties of the object
    def display_properties(self):
        print(f"Color: {self.color}")
        print(f"Max Speed: {self.max_speed} kmph")
        print(f"Mileage: {self.mileage} kmpl")
        print(f"Seating Capacity: {self.seating_capacity}")
        print("-" * 30)


# Testing Problem 4
# Task-5: Create two objects with specified properties
car1 = Vehicle(200, 20)
car1.set_seating_capacity(5)

car2 = Vehicle(180, 25)
car2.set_seating_capacity(4)

print("\n--- Car 1 Properties ---")
car1.display_properties()

print("--- Car 2 Properties ---")
car2.display_properties()
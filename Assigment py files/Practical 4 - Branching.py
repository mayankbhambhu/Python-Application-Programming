#Q1: Check Lionel Messi's Achievements
# Output depends on the contents of the undefined 'players' list.
for player in players:
    if player["name"] == "Lionel Messi":
        if player["achievements"] > 10:
            print(f"Name: {player['name']}, Sport: {player['sport']}, Achievements: {player['achievements']}")
        else:
            print(f"{player['name']} does not have more than 10 achievements.")

#Q2: Tennis Player or Exactly 20 Achievements
# Output depends on the contents of the undefined 'players' list.
for player in players:
    if player["sport"] == "Tennis" or player["achievements"] == 20:
        print(f"Success! {player['name']} meets the criteria.")

#Q3: Less than 10 Achievements and Not Soccer
# Output depends on the contents of the undefined 'players' list.
for player in players:
    if player["achievements"] < 10 and player["sport"] != "Soccer":
        print(f"Details: {player['name']} | Sport: {player['sport']} | Achievements: {player['achievements']}")

#Q4: Number Properties Analysis (1 to 9999)
num = int(input("Enter an integer (1 to 9999): "))
# Output depends on user input. For example, if input is 121:

# 1. Even or Odd
if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")
# Output (if 121): 121 is Odd.

# 2. Palindrome Check
num_str = str(num)
if num_str == num_str[::-1]:
    print(f"{num} is a Palindrome.")
else:
    print(f"{num} is not a Palindrome.")
# Output (if 121): 121 is a Palindrome.

# 3. Divisibility by Sum of Digits
digit_sum = sum(int(digit) for digit in num_str)
if num % digit_sum == 0:
    print(f"{num} is divisible by the sum of its digits ({digit_sum}).")
else:
    print(f"{num} is not divisible by the sum of its digits ({digit_sum}).")
# Output (if 121): 121 is not divisible by the sum of its digits (4).

#Q5: Print Range from -5 to 5
for i in range(-5, 6):
    print(i)
# Output:
# -5
# -4
# -3
# -2
# -1
# 0
# 1
# 2
# 3
# 4
# 5

#Q6: Print List Elements
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for square in squares:
    print(square)
# Output:
# red
# yellow
# green
# purple
# blue

#Q6: Print List Elements (Duplicated in original file)
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for square in squares:
    print(square)
# Output:
# red
# yellow
# green
# purple
# blue

#Q7: Copy 'orange' Strings Using While Loop
squares = ['orange', 'orange', 'red', 'yellow', 'orange']
new_squares = []
i = 0

while i < len(squares) and squares[i] == 'orange':
    new_squares.append(squares[i])
    i += 1

print("new_squares:", new_squares)
# Output: new_squares: ['orange', 'orange']

#Q8: Filter 7-Letter Animal Names Using While Loop
Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile", "deer", "swan"]
seven_letter_animals = []
i = 0

while i < len(Animals):
    if len(Animals[i]) == 7:
        seven_letter_animals.append(Animals[i])
    i += 1

print("Animals with 7 letters:", seven_letter_animals)
# Output: Animals with 7 letters: ['giraffe', 'gorilla', 'parrots']
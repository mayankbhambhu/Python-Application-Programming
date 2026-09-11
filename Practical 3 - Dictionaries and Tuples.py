#
# Part A - Dictionaries
#


# 1. Create an empty Dictionary
inventory = {}
# 2. Store the first product details in variables
p1_name = "Mobile Phone"
p1_quantity = 5
p1_price = 20000
p1_release_year = 2020
# 3. Add details in inventory
inventory["Product1"] = {
    "Name": p1_name,
    "Quantity": p1_quantity,
    "Price": p1_price,
    "ReleaseYear": p1_release_year
}
# 4. Store the Second Product details in variables
p2_name = "Laptop"
p2_quantity = 3
p2_price = 55000
p2_release_year = 2022
# 5. Add the item details in inventory
inventory["Product2"] = {
    "Name": p2_name,
    "Quantity": p2_quantity,
    "Price": p2_price,
    "ReleaseYear": p2_release_year
}
# 6. Display the products present in inventory
print("--- Initial Inventory ---")
print(inventory)

# Output:  --- Initial Inventory ---
#.         {'Product1': {'Name': 'Mobile Phone', 'Quantity': 5, 'Price': 20000, 'ReleaseYear': 2020}, 'Product2': {'Name': 'Laptop', 'Quantity': 3, 'Price': 55000, 'ReleaseYear': 2022}}


# 7. Check if ProductNo1_releaseYear and ProductNo2_releaseYear are in inventory
p1_has_year = "ReleaseYear" in inventory["Product1"]
p2_has_year = "ReleaseYear" in inventory["Product2"]

print(f"\nProduct 1 has ReleaseYear: {p1_has_year}")
print(f"Product 2 has ReleaseYear: {p2_has_year}")

# Output: Product 1 has ReleaseYear: True
#         Product 2 has ReleaseYear: True

# 8. Delete release year of both the products from the inventory
del inventory["Product1"]["ReleaseYear"]
del inventory["Product2"]["ReleaseYear"]

print("\n--- Inventory After Deleting Release Years ---")
print(inventory)

# Output:    --- Inventory After Deleting Release Years --- 
#           {'Product1': {'Name': 'Mobile Phone', 'Quantity': 5, 'Price': 20000}, 'Product2': {'Name': 'Laptop', 'Quantity': 3, 'Price': 55000}}

#
#
# Part B - Tuples
#
#

# 1. Create a tuple called prices
prices = (250, 300, 150, 400, 100, 350, 200)

# 2. Find and print the highest and lowest price
highest_price = max(prices)
lowest_price = min(prices)
print(f"Highest Price: {highest_price}")
print(f"Lowest Price: {lowest_price}")

# output: Highest Price: 400
#         Lowest Price: 100

# 3. Calculate and print the total sum of all prices
total_sum = sum(prices)
print(f"Total Sum of Prices: {total_sum}")
# output: Total Sum of Prices: 1750

# 4. Convert the tuple into a sorted list (ascending order) and print it
sorted_prices = sorted(prices)
print(f"Sorted List of Prices: {sorted_prices}")

# output: Sorted List of Prices: [100, 150, 200, 250, 300, 350, 400]


# 5. Try to modify an element in the tuple
try:
    prices[0] = 500  # Attempting to change the first element
except TypeError as e:
    print(f"\nModification Error: {e}")
    
# output: Modification Error: 'tuple' object does not support item assignment
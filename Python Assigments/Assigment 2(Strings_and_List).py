#1.Create an empty list.
shopping_list = []

#2.Now store the number of items in shopping list:
#    Watch, laptop, shoes, pen, clothes.
shopping_list =["Watch", "Laptop", "Shoes", "Pen", "Clothes"]

#3.Add new item Football to the shopping list.
shopping_list.append("Football")

#4.Print Last Item from the shopping list.
print("Last item:", shopping_list[-1])
# Output: Last item: Football

#5.Print entire shopping list.
print("Shopping List:", shopping_list)
# Output: Shopping List: ['Watch', 'Laptop', 'Shoes', 'Pen', 'Clothes', 'Football']

#6.Print the important items like laptop and shoes from the shopping list.
print("Important items:", shopping_list[1], "and", shopping_list[2])
# Output: Important items: Laptop and Shoes

#7.Change the item: Instead of pen now I want to buy notebook.
shopping_list.remove("Clothes")

#8.Print the entire shopping list by deleting the least important item.
print("Final Shopping List:", shopping_list)
# Output: Final Shopping List: ['Watch', 'Laptop', 'Shoes', 'Pen', 'Football']
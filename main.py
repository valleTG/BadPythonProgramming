# Imports

import time

# While Loops

# name = None

# while not name:
#     name = input("Enter your name: ")

# print("Hello " + name)

# For Loops

# for i in range(10):
#     print(i + 1)

# for i in range(50, 100 + 1, 2):
#     print(i)

# for i in "Valle TG":
#     print(i)

# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")

# Nested Loops

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")

# Break, Continue, Pass

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-7890"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1, 20 + 1):

#     if i == 13:
#         print("Unlucky number! Skipping it.")
#         pass

#     else:
#         print(i)

# Lists

# food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

# food[0] = "sushi"

# food.append("ice cream")
# food.remove("hotdog")
# food.pop()
# food.insert(0, "cake")
# food.sort()
# food.clear()

# for x in food:
#     print(x)

# 2D Lists

# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]

# food = [drinks, dinner, dessert]

# print(food[2][1])

# Tuples

# student = ("Valle", 15, "Male")

# print(student.count("Valle"))
# print(student.index("Male"))

# for x in student:
#     print(x)

# if "Valle" in student:
#     print("Valle is here")

# Sets

# utensils = {"Fork", "Spoon", "Knife"}
# dishes = {"Bowl", "Plate", "Cup", "Knife"}

# utensils.add("Napkin")
# utensils.remove("Fork")
# utensils.clear()
# dishes.update(utensils)
# dinner_table = utensils.union(dishes)

# print(dishes.difference(utensils))
# print(utensils.intersection(dishes))

# for x in dishes:
#     print(x)


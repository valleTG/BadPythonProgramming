# Imports

import time
import math

# Variables

# first_name = "Valle"
# last_name = "TG"
# full_name = first_name +" "+ last_name
# print("Hello " + first_name)
# print(type(first_name))

# age = 15
# age += 1
# print("Your age is:  " + str(age))
# print(type(age))

# height = 250.5
# print("Your height is: " + str(height) + "cm")
# print(type(height))

# human = True
# print("Are you a human: " + str(human))
# print(type(human))

# Multiple Assignment

# name = "Valle"
# age = 15
# attractive = True

# name, age, attractive = "Valle", 21, True

# print(name)
# print(age)
# print(attractive)

# Spongebob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30

# Spongebob = Patrick = Sandy = Squidward = 30

# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)

# String Methods

# name = "Valle"

# print(len(name))
# print(name.find("a"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("a"))
# print(name.replace("a", "o"))
# print(name * 3)

# Type Casting

# x = 1  # Int
# y = 2.0  # Float
# z = "3"  # String

# x = str(x)
# y = str(y)
# z = str(z)

# print(x)
# print(y)
# print(z * 3)

# User Input

# name = input("What is your name?; ")
# age = int(input("How old are you?: "))
# height = float(input("How tall are you?: "))

# print("Hello " + name)
# print("You are " + str(age) + " " + "years old")
# print("You are " + str(height) + "cm tall")

# Math Functions

# pi = 3.14
# x = 1
# y = 2
# z = 3

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi, 2))
# print(math.sqrt(420))
# print(max(x, y, z))
# print(min(x, y, z))

# String Slicing

# name = "Valle TG"

# first_name = name[:3]
# last_name = name[4:]
# funky_name = name[::2]
# reversed_name = name[::-1]

# print(reversed_name)

# website1 = "http://google.com"
# website2 = "http://wikipedia.com"

# slice = slice(7, -4)

# print(website1[slice])
# print(website2[slice])

# If Statements§

# age = int(input("How old are you?: "))

# if age == 100:
#     print("You are a century old!")
# elif age >= 18:
#     print("You are an adult!")
# elif age <0:
#    print("You haven't been born yet!")
# else:
#     print("You are a child!")

# Logical Operators

# temp = int(input("What is the temperature outside?: "))

# if 0 <= temp <= 30:
#     print("The temperature is good today!")
#     print("Go outside!")

# elif temp < 0 or temp > 30:
#    print("The temperature is bad today!")
#     print("Stay inside!")

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

# Dictionaries

# capitals = {'Sweden': 'Stockholm',
#             'USA': 'Washington DC',
#             'China': 'Beijing',
#             'Russia': 'Moscow'}

# capitals.update({'Germany': 'Berlin'})
# capitals.update({'USA': 'Las Vegas'})
# capitals.pop('China')
# capitals.clear()

# print(capitals["Germany"])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key, value in capitals.items():
#     print(key, value)

# Indexing

# name = "valle TG!"

# if name[0].islower():
#     name = name.capitalize()

# first_name = name[:5].upper()
# last_name = name[6:].lower()
# last_character =  name[-1]

# print(first_name)
# print(last_name)
# print(last_character)

# Functions

# def hello(first_name, last_name, age):
#     print("Hello " + first_name + " " + last_name + "!")
#     print("You are " + age + " " + "years old!")
#     print("Have a good day!")


# hello("Linus", "Rudhage",  str(15))

# Return Statements

# def  multiply(number1, number2):
#    return number1 * number2


# num1 = int(input("Enter first number to multiply here: "))
# num2 = int(input("Enter second number to multiply here: "))

# result = multiply(num1, num2)
# print(result)
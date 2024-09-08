# Exercise 6
# Question 1

import random
import math

def dice_roll():
    return random.randint(1,6)
while True:
    dice = dice_roll()
    print(f"Dices eyes are: {dice}")
    if dice == 6:
        break

# Question 2

def dice_roll_side (num):
    return random.randint(1,num)

num = int(input("How many sides in your dice?"))
while True:
    dice = dice_roll_side(num)
    print(f"Your dice are: {dice}")
    if dice == num:
        break

# Question 3

def gallons_to_liters(gallons):
    return 3.7854 * gallons

while True:

    gallons = float(input("How many gallons do you need to convert?"))
    if gallons < 0:
        break
    print(f"{gallons}gallons are {gallons_to_liters(gallons):.1f} liters. ")

    break


# Question 4

def sum(numbers_list):
    total = 0
    for i in numbers_list:
        total += i
    return total
ex_list = []
for num in range(10):
    ex_list.append(random.randint(1,10))

print(f"The list of numbers is:", end="")

for i in ex_list:
    print(f"{i}", end="")
print(f"\nThe sum of all items in the list is : {sum(ex_list)}")

# Question 5

def even_num_list(x):
    even = []
    for n in x:
        if not n % 2 == 0:
            even.append(n)
    return even

num = [0,1,2,3,4,5,6,7,8,9,10,20,25,30,47,67,68,80]

print("Uneven numbers")
print(even_num_list(num))

# Question 6

def pizza_efficiency(d, price):
    return price/math.pi * (d/200.) ** 2
pizza1_diameter = float(input("What is the diameter of the pizza in centimeters?"))
pizza1_price = float(input("What is the price of the pizza in euros?"))
pizza2_diameter = float(input("What is the diameter of the pizza in centimeters?"))
pizza2_price = float(input("What is the price of the pizza in euros?"))

if pizza_efficiency(pizza1_diameter, pizza1_price) > pizza_efficiency(pizza2_diameter, pizza2_price):
    print("The first pizza is a good!")
else:
    print("The second pizza is a good!")


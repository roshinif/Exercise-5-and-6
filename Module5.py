# Exercise 5
# Question 1

import random
number_dice = int(input("How many dice to roll?"))
sum = 0
for i in range(number_dice):
    roll = random.randint(1,6)
    sum += roll
    print(sum)

# Question 2

numb = []
while True:
    input_number = input("Enter a number: ")
    if input_number == "":
        break

    numb.append(int(input_number))
numb.sort(reverse=True)
print("The five greatest numbers sorted in descending order",
      numb[:5])

# Question 3

def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
numbers = int(input("Enter an integer:"))
if prime_number(numbers):
    print("The number is prime")
else:
    print("The number is not prime")

# Question 4

print("Enter the names of five cities one by")
cities = []
for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    cities.append(city)
print("\nEntered cities:")
for city in cities:
    print(city)


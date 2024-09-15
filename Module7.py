# Exercise 7
# Question 1

import random

seasons = ("Spring", "Summer", "Autumn", "Winter")
month= int(input("Enter the month number (1-12): "))

if month in [1,2,3]:
    season = seasons[0]
if month in [4,5,6]:
    season = seasons[1]
if month in [7,8,9]:
    season = seasons[2]
if month in [10,11,12]:
    season = seasons[3]

print(f"The season is: {season}")

# Question 2

name = set()

while True:
    your_name = input("Enter your name:")

    if your_name =="":
        break

    if your_name in name:
        print("Existing name")
    else:
        print("New name")
        name.add(your_name)

print("\nAll names entered:")
for your_name in name:
    print(your_name)


# Question 3

airport_dict = {}

def add_airport():
    name = input ("Enter your airport name:")
    icao_code = input("Enter the icao code:")

    if icao_code in airport_dict:
        print("this airport is already added to the databse.")
    else:
        airport_dict[icao_code] = name
        print(f"Airport {name} and ICAO code {icao_code} have been added.")

def fetch_the_airport():
    icao_code = input("Input the Airport's ICAO code:")

    if icao_code in airport_dict:
        print(f"The name of the Airport and ICAO code {icao_code} is: {airport_dict[icao_code]}")
    else:
        print("This ICAO code is not available.")

def main():
    while True:
        print("Choose an option:")
        print("(1). Enter a new airport")
        print("(2). Fetch the information of an airport")
        print("(3). Quit")

        number = int(input("Enter the number (1,2,3):"))
        if number == 1:
            add_airport()
        elif number == 2:
            fetch_the_airport()
        elif number == 3:
            print("Quit")
            break

main()
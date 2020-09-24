#!/usr/bin/env python3
import sys

message = "very sad to meet a quitter like you"
def sum():
    print("Try paper and pencil next time window face..")
    while True:
        try:
            print("Press q to quit..")
            list = input("Enter numbers separated by commas : ")
            if list.lower() == "q":
                return message
            working_list = list.split(",")
            total = 0
            for num in working_list:
                total += float(num)
            break
        except:
            print("Beeeep!! Let's try again Swampy")
    return round(total,2)

def subtract():
    num1 = 0.0
    num2 = 0.0
    while True:
        try:
            print("Press q to quit..")
            num1 = input("Enter first number, you lazy bum: ")
            if num1.lower() == "q":
                return message
            num1 = float(num1)
            num2 = input("Enter second number now: ")
            if num2.lower() == "q":
                return message
            num2 = float(num2)
            break
        except:
            print("Beeeep!! Let's try again Lord of the Jinx")
    return round(num1-num2,2)

def divide():
    num1 = 0.0
    num2 = 0.0
    while True:
        try:
            print("Press q to quit..")
            num1 = input("Hurry up and enter numerator, I dont have time: ")
            if num1.lower() == "q":
                return message
            num1 = float(num1)
            num2 = input("Enter denominator now poopypants: ")
            if num2.lower() == "q":
                return message
            num2 = float(num2)
            break
        except:
            print("Beeeep!! Let's try again dead skunk")
    return round(num1 / num2, 2)

def multiply():
    while True:
        try:
            print("Press q to quit..")
            list = input("Enter numbers separated by commas [eg:1,2,3,4] : ")
            if list.lower() == "q":
                return message
            working_list = list.split(",")
            product = 1
            for num in working_list:
                product *= float(num)
            break
        except:
            print("Beeeep!! Let's try again Karen")
    return round(product,2)

def main():
    print("\t\t\t\tRude Calculator")
    while True:
        try:
            user_input = input("What do you want to do sh*thead? [add, subtract, divide or multiply}: ")
            user_input = user_input.lower()
            if user_input == "q":
                print("Dont come back again")
                return
            if user_input == "add":
                print(f"Sum is {sum()}")
                break
            elif user_input == "subtract":
                print(f"Difference is {subtract()}")
                break
            elif user_input == "divide":
                print (f"Division result is {divide()}")
                break
            elif user_input == "multiply":
                print (f"Product is {multiply()}")
                break
        except:
            print("Let's try again noodle fingers")
main()

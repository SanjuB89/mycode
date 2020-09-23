#!/usr/bin/env python3

#easy
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for animal in farms[0]["agriculture"]:
    print(animal)

#medium

while True:
    user_input = input("Choose a farm: [NE Farm, W Farm, SE Farm]:: ")
    user_input = user_input.lower()
    if user_input == 'ne farm':
        for animal in farms[0]["agriculture"]:
            print(animal)
        break
    elif user_input == 'w farm':
        for animal in farms[1]["agriculture"]:
            print(animal)
        break
    elif user_input == 'se farm':
        for animal in farms[2]["agriculture"]:
            print(animal)
        break
    else:
        print("Try the given options")

#hard

while True:
    animals =["sheep", "cows", "pigs", "llamas", "cats", "chickens"]
    user_input = input("Choose a farm: [NE Farm, W Farm, SE Farm]:: ")
    user_input = user_input.lower()
    if user_input == 'ne farm':
        for elem in farms[0]["agriculture"]:
            if elem in animals:
                print(elem)
        break
    elif user_input == 'w farm':
        for elem in farms[1]["agriculture"]:
            if elem in animals:
                print(elem)
        break
    elif user_input == 'se farm':
        for animal in farms[2]["agriculture"]:
            if elem in animals:
                print(elem)
        break
    else:
        print("Try the given options")

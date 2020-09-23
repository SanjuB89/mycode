#!/usr/bin/env python3

#for Counter

plate = ["chicken", "potato", "pizza", "broccoli"]

for food in plate:
    if food == "broccoli":
        print("Bring your face over here. I am going to slap you")

#for Delete

items = ["trash can", "painting", "barbie", "teddy"]
toys = ["barbie", "teddy", "plastic trinasaur"]

for elem in items:
    if elem in toys:
        print("Trashed your " + elem)
        items.remove(elem)
print(items)

#for Add

report_card = {"science": "A", "maths": "B", "history": "F", "physics": "F"}

number_of_snakes = 0

for grade in report_card.values():
    if grade == "F":
        number_of_snakes += 1

print(f"I threw {number_of_snakes} snakes on your bed")




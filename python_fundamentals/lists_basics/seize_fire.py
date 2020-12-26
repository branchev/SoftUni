#BAKERY

import math

def percentage(total, compete):
    if total < compete:
        percents = (total - compete)/compete * 100
        print(f"You produce {abs(percents):.2f} percent less biscuits.")
    else:
        percents = (compete - total)/compete * 100
        print(f"You produce {abs(percents):.2f} percent more biscuits.")


biscuits_per_worker = int(input())
workers = int(input())

normal_day_production = workers * biscuits_per_worker

third_day_production = workers * biscuits_per_worker * 0.75
third_day_production = math.floor(third_day_production)

total = normal_day_production * 20 + third_day_production * 10

compete_factory_production = int(input())

print(f"You have produced {total} biscuits for the past month.")

percentage(total, compete_factory_production)

# LOOOT
Angry Pet
Tom is very angry with his owner, because he left him alone during the teamwork defenses for the Programming Fundamentals Course at SoftUni. It’s time for Tom to get his payback and he will do it, by breaking various household items.
Each item has a price rating which is a number that describes how valuable is that item for Tom’s owner. You will be given an entry point from which Tom will start breaking the items to his left, and then to his right. Tom will never break the item at the entry point. 
You must calculate the damage to both his left, and right, then print only the higher (bigger) damage to the household. If both sums are equal print the left one.
Input / Constrains
•	On the first line you will receive the price ratings, separated by (space). Each element will be integer in range [-231… 231]
•	On the second line you will receive the entry point, which will always be between the second and the penultimate element in the array
•	On the third line you will receive the type of items Tom wants to break, which will be one of the following:
o	cheap – items that have lower price rating than the entry point item
o	expensive – items that have same price rating, or higher price rating than the entry point item
•	On the last line you will receive the type of price ratings that Tom will look for, which will be one of the following:
o	positive – price ratings above 0
o	negative – price ratings below 0
o	all – any price ratings
Output
•	Single line containing the sum of price ratings and their position based on the entry point in the following format:
o	"{position} – {sum of price ratings}"
Angry Pet
Tom is very angry with his owner, because he left him alone during the teamwork defenses for the Programming Fundamentals Course at SoftUni. It’s time for Tom to get his payback and he will do it, by breaking various household items.
Each item has a price rating which is a number that describes how valuable is that item for Tom’s owner. You will be given an entry point from which Tom will start breaking the items to his left, and then to his right. Tom will never break the item at the entry point. 
You must calculate the damage to both his left, and right, then print only the higher (bigger) damage to the household. If both sums are equal print the left one.
Input / Constrains
•	On the first line you will receive the price ratings, separated by (space). Each element will be integer in range [-231… 231]
•	On the second line you will receive the entry point, which will always be between the second and the penultimate element in the array
•	On the third line you will receive the type of items Tom wants to break, which will be one of the following:
o	cheap – items that have lower price rating than the entry point item
o	expensive – items that have same price rating, or higher price rating than the entry point item
•	On the last line you will receive the type of price ratings that Tom will look for, which will be one of the following:
o	positive – price ratings above 0
o	negative – price ratings below 0
o	all – any price ratings
Output
•	Single line containing the sum of price ratings and their position based on the entry point in the following format:
o	"{position} – {sum of price ratings}"

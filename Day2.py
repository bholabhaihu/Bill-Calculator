# Bill Calculator
print("Welcome to the tip calculator.")
bill = int(input("What was the total bill? Rs "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
total = bill * (tip / 100)  + bill
people = int(input("How many people to split the bill? "))
split = (total / people)
print("Each person should pay", str(round(split, 2)))
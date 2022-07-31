print("Welcome to the tip calculator.")
sum_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
bill_with_percent = ((sum_bill/100) * percentage_tip + sum_bill)
is_how_many_people_to_split = int(input("How many people to split to the bill?"))

total = round(bill_with_percent / is_how_many_people_to_split, 2)

print(f"Each person should pay: ${total}")
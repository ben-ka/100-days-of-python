print("welcome to the tip calculator")
total_bill = float(input("total bill? $"))
people_split = int(input("how many people to split the bill? "))
precent_tip = int(input("what precentage would you like to give? %"))
total_pay = total_bill+total_bill*precent_tip/100
pay_each = total_pay /people_split
print(f"each person should pay ${pay_each}")
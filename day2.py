print("Welcome to tip calculator!")
bill = float(input("Enter your bill amount\n$ "))
tip = int(input("How much tip you want to give?\nPercent "))
split = int(input("How many people to split the bill?\nPeople "))

total = ("{:.2f}".format((((bill * (tip/100)) + bill)/split)))
print(f"Each person should pay ${total}.")
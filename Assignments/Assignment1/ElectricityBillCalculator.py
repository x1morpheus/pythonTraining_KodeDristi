units = float(input("Enter the number of units consumed: "))

if units <= 10:
    bill = units * 0.50
elif units <= 50 and units > 10:
    bill = 25*0.50 + (units - 50) * 0.75
elif units <= 100 and units > 50:
    bill = 50*0.75 + (units - 100) * 1
else:
    bill = 100*1 + (units - 100) * 1.50

print(f"The electricity bill is: NPR {bill:.2f}")
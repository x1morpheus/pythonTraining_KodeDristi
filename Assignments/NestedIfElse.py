a = float(input("Enter a first number: "))
b = float(input("Enter a second number: "))
c = float(input("Enter a third number: "))

if a >= b:
    if a >= c:
        print(f"The largest number is: {a}")
    else:
        print(f"The largest number is: {c}")
else:
    if b >= c:
        print(f"The largest number is: {b}")
    else:
        print(f"The largest number is: {c}")
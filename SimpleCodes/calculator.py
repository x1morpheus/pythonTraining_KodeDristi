
while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("calculations: ")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit")

    choice = input("Choose an operation (1/2/3/4/5): ")

    if choice == '1':
        print("Addition: ",a + b)
    elif choice == '2':
        print("Subtraction ",a - b)
    elif choice == '3':
        print("Multiplication: ",a * b)
    elif choice == '4':
        if b != 0:
            print("Division: ",a / b)
        else:
            print("Error: Division by zero is not allowed.")
            break
    elif choice == 5:
        break
    else:
        print("Invalid input")


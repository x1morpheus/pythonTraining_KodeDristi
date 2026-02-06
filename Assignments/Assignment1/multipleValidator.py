#5. Write a program to determine whether a number is a multiple of both 3 and 5.

a = float(input("Enter a number: "))


if a%3 ==0 and a%5==0:
    print(f"{a} is a multiple of both 3 and 5.")
else:
    print(f"{a} is not a multiple of both 3 and 5.")
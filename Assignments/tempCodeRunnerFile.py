#1. Write a program to assign grades based on marks:

#A for ≥ 90
#B for ≥ 75
#C for ≥ 60
#Fail for < 60


a = float(input("Enter your Grade: "))

if(a <60):
    grade ="Fail"
elif(a>=60 and a<75):
    grade = "C"
elif(a>=75 and a<90):
    grade = "B"
elif(a>=90 and a<=100):
    grade = "A"
else:
    grade = "Invalid Grade"

print(f"Your grade is: {grade}")
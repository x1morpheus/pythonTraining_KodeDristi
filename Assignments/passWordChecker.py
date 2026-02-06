a = input("Enter your password: ")
if len(a) < 8:
    print("Password is weak")
elif len(a) > 8 and len(a) < 12:
    print("Password is medium")
else:
    print("Password is strong")
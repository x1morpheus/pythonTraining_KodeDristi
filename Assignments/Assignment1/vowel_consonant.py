#2. Write a program to check whether a given character is a vowel or consonant.

char = input("Enter a character: ").lower()

vowels = ['a', 'e', 'i', 'o', 'u']

if char in vowels:
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")

letter = input("Enter a letter: ")


if len(letter) == 1 and letter.isalpha():
    if letter.lower() in "aeiou":
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is not a vowel.")
else:
    print("Invalid input. Please enter a single letter.")

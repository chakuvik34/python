
i = input("Enter a string: ")
char_frequency = {}


for char in i:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print("Character frequencies in the string:")
for char, count in char_frequency.items():
    print(f"'{char}' occurs {count} times")

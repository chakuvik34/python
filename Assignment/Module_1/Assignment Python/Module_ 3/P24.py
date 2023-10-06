
a = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 5}
b = input("Enter a key to check: ")

if b in a:
    print(f"{b} exists in the dictionary {a[b]}")
else:
    print(f"{b} does not exist in the dictionary")

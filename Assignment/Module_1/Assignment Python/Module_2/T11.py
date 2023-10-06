
n = int(input("Enter a num: "))
a =0
if n <= 0:
    print("Please enter num .")
else:
    for i in range(1, n + 1):
        a += i

    print(f"The sum of positive integers is: {a}")

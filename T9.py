
a = int(input("Enter the first integer: "))
b= int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))


if a == b or b == c or a == c:
    result =0
else:
    result = a + b + c

print(f"The sum is: {result}")

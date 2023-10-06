s1 = input("Enter the first string: ")
s2= input("Enter the second string: ")

swapped_s1 = s2[:2] + s1[2:]
swapped_s2 = s1[:2] + s2[2:]

ans = swapped_s1 + ' ' + swapped_s2

print(f"The result string is: {ans}")

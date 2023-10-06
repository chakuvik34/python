s = input("Enter a string: ")

if len(s) >= 3 and not s.endswith('ing'):
    s1 = s + 'ing'
    
elif s.endswith('ing'):
    s1 = s + 'ly'
else:
    s1 = s

print(f"The modified string is: {s1}")

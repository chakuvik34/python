
input_str = input("Enter a list of values separated by spaces: ")
user_list = input_str.split()
if len(user_list) >= 3:
    var1, var2, var3 = user_list[:3]
    print("var1:", var1)
    print("var2:", var2)
    print("var3:", var3)
else:
    print("Please enter at least 3 values in the list to split.")

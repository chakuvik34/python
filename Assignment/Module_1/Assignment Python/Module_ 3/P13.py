
input_str = input("Enter tuple elements separated by spaces: ")
elements = input_str.split()
user_tuple = tuple(elements)
result_string = ''.join(user_tuple)
print("Converted String:", result_string)

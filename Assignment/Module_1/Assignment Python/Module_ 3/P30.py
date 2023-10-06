
def key_exists(input_dict, key):
    return key in input_dict

example_dict = {'a': 1, 'b': 2, 'c': 3}

user_key = input("Enter a key to check: ")

if key_exists(example_dict, user_key):
    print(f"The key '{user_key}' exists in the dictionary.")
else:
    print(f"The key '{user_key}' does not exist in the dictionary.")

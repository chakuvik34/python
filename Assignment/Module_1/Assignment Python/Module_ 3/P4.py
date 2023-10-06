
def is_list_empty(input_list):
    return not bool(input_list)

my_list = []

if is_list_empty(my_list):
    print("The list is empty.")
else:
    print("The list is not empty.")



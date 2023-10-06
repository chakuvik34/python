
def have_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

input_list1 = input("Enter the first list : ").split()
input_list2 = input("Enter the second list: ").split()


list1 = [int(item) for item in input_list1]
list2 = [int(item) for item in input_list2]


if have_common_member(list1, list2):
    print("The two lists in one common.")
else:
    print("The two lists do common member.")

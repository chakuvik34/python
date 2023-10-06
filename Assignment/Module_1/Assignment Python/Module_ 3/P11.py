l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2= [3, 4, 5,9]
if all(item in l1 for item in l2):
    print("l1 contains l2.")
else:
    print("l1 does not contain l2.")

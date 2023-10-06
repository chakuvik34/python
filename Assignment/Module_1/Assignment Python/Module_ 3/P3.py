
a= input("Enter a list : ")

l = a.split(',')

l = [value.strip() for value in l]

unique_list = list(set(l))

print("List with Duplicates Removed:", unique_list)

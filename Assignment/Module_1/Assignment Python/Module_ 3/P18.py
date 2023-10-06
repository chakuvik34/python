
tuple = (1, 2, 2, 3, 4, 4, 5, 6, 6)

r1 = set()
u1 = set()

for item in tuple:
    if item in u1:
        r1.add(item)
    else:
        u1.add(item)


r1_list = list(r1)
print("Repeated Items:", r1_list)


my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 150, 'e': 250}

sorted_items = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

highest_3 = sorted_items[:3]

print("Highest 3 Values:")
for key, value in highest_3:
    print(f"{key}: {value}")

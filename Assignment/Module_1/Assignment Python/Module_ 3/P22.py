
a = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 5}
b = dict(sorted(a.items(), key=lambda item: item[1]))

c= dict(sorted(a.items(), key=lambda item: item[1], reverse=True))
print("Ascending:",b)
print("Descending:",c)

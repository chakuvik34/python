d={901:"hiteshi",888:"jalpa",657:"savan",456:"akash"}
print(d)
print(d[888])
print(d.get(657))
print(d.items())
print(d.keys())
print(d.values())
d.pop(657)
print(d)
d.popitem()
print(d)
d1={101:"jigar",202:"sunil",303:"jay"}
d.update(d1)
print(d)

for i in d:
    print(i," : ",d[i])

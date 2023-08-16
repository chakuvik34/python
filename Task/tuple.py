t=(1,2,3,1.1,2.2,"tops",True,"java",[10,20,30],"python",10,1,2)
print(t)

print(t.count(1))
print(t.index(10))

for i in t:
    print(i)
print(10 in t)    
print (t[8])
t[8].append(40)
print(t)

L=[1,2,3,1.1,2.2,"Tops",True,False,1,10,"python",1]
print(L)
L.append(100)
print(L)
# L.clear()
print(L)
L1=L.copy()
print(L1)
L1.append(200)
print(L1)
L=L1
print(L1)
print(L)
print(L.count(1))

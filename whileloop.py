
n=int(input("Enter N:"))
while n>0:
 print("Tops Technologies")
 n=n-1

 n=int(input("Enter N:"))
 sum=0
 while n>0:
     sum=sum+n
     n=n-1
print("sum: ",sum)   


for i in range(1,10):
    if i==5:
        continue
    else:
         print("I: ",i)

         
for i in range(1,10):
    if i==5:
        break
    else:
        print("I: ",i)


s="Tops Technologies"
print(len(s))
print(s.casefold())
print(s.capitalize())
print(s.lower())
print(s.upper())
print(s.center(40,"*"))
print(s.count("o"))
print(s.endswith("es"))
print(s.startswith("To"))
print(s.find("logi"))
print(s.index("T"))
print(s.index("T",2))
print("Tops123".isalnum())
print("Tops".isalpha())
print("123".isnumeric())
print(s.istitle())
print(s.swapcase())
print(" ".isspace())



import random
data=open("data.txt","w")
for i in range(10):
    num=random.randint(1,100)
    data.write(str(num)+",")
data.close()

data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")
prime=open("prime.txt","w")
l=data.read().split(",")[:-1]
for i in l:
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")
    if int(i)%2!= 0:
        for j in range(3,int(int(i)/2)+1,2):
            if int(i)%j==0:
                break
            else:
                prime.write(i+",")
        
data.close()        
even.close()        
odd.close()
prime.close()

print("data file contact")
data=open("data.txt","r")
print(data.read())
data.close()


print("even file contact")
data=open("even.txt","r")
print(data.read())
data.close()


print("odd file contact")
data=open("odd.txt","r")
print(data.read())
data.close()
        
                
print("prime file contact")
data=open("prime.txt","r")
print(data.read())
data.close()


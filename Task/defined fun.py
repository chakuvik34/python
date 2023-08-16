#function with no argument and no return value.

def printLine():
    print("*"*60)

printLine()
print("welcome to user defined function in python.")
printLine()

#function with argument but no return value.

def add(a,b):
    print("Addition : ",a+b)

printLine()
x=int(input("Enter value : "))
y=int(input("Enter value : "))
add(x,y)
printLine()

#function with  argument and return value.

def sub(a,b):
    return a-b

printLine()
x=int(input("Enter value : "))
y=int(input("Enter value : "))
print("subtraction : ",sub(x,y))
printLine()


    

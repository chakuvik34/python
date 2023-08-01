import udf


while True:
    print("*************************************************")
    print("1. Odd Even")
    print("2. Max Of Two")
    print("3. Max Of Three")
    print("4.Prime")
    print("5.Fibonacci")
    print("6.Excit")
    print("*************************************************")
    choice=int(input("Enter Your Choice : "))
    print("*************************************************")
    if choice ==1:
       a=int(input("Enter Number : "))
       udf.oddeven(a)
       print("*************************************************")
    elif choice==2:
        a=int(input("Enter Number : "))
        b=int(input("Enter Number : "))
        udf.maxoftwo(a,b)
        print("*************************************************")
    elif choice==3:
        a=int(input("Enter Number : "))
        b=int(input("Enter Number : "))
        c=int(input("Enter Number : "))     
        udf.maxofhree(a,b,c)
        print("*************************************************")
    elif choice==4:
        a=int(input("Enter Number : "))
        udf.prime(a)
        print("*************************************************")
    elif choice==5:
        a=int(input("Enter Number : "))
        udf.fibonacci(a)
        print("*************************************************")
    elif choice==6:
        print("Thnnk You For Using Our Services.")
        break
    else:
        print("Invalid Choice. Please Try Again.")
        print("*************************************************")            




              

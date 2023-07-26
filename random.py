import random
#print (random.randint(1000,9999))
#print (random.choice([1,2,3,"tops","java","python",10,True]))      

num=random.randint(1,20)

while True:
    guess=int(input("guess A number between 1 to 2 : "))
    if guess==num:
        print("you guess a correct number")
        break
    elif guess>num:
        print("you guess a greater number")
    elif guess<num:
        print("you guess a smaller number")

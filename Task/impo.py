import random

#print(random.randint(1,200))
#print(random.choice([10,20,"python","java",10,True]))

num=random.randint(1,20)

while True:
    guess=int(input("Guess A Number Between 1 to 20 : "))
    if guess==num:
        print("you Guessed A Correct Number")
        break
    elif guess>num:
        print("you Guessed A Greter Number")

    elif guess>num:
        print("you Guessed A smaller Number")
        
    

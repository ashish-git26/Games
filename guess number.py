import random

i=random.randrange(0,100)

c=0
while c<7:
    gu=int(input("Enter a number between 1-100:"))
    if gu==i:
        print("Your Guess is Correct",gu)
        break;
    else:
        if i<gu:
            print("Guess is high")
        else:
            print("Guess is low")
    c+=1

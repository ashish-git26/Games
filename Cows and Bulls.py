import random
g=random.randint(100,999)
s=str(g)
ch=0
while ch<10:
    gu=int(input("Enter your guess:"))
    co=str(gu)
    if gu==g:
        print("Congrats Your guess was correct",gu)
        break;
    else:
        cows=0
        bulls=0
        for i in co:
            if i in s and co.index(i)==s.index(i):
                bulls+=1
            elif i in s:
                cows+=1
        print("Cows=",cows,"\nBulls=",bulls)
    ch+=1
if ch==10:
    print("You lost! The guess was",g)
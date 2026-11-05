import random
a=random.randint(1000,9999)
d=str(a)
l2=["_","_","_","_"]
def dis(n):
    l=["_______",
       "   |   ",
       "   O   ",
       "  /|\  ",
       "  / \  ",]
    for j in range(n):
        print(l[j])
k=0
while True:
    b=int(input("Enter a number:"))
    c=str(b)
    if a==b :
        print("Your guess is correct",a)
        break;
    else:
        ch=False
        for i in c:
            if i in l2:
                pass
            elif i in d:
                l2[d.index(i)]=i
                ch=True
        if ch==False:
            k+=1
        dis(k)
        print(l2)
        if k==5:
            print("you cannot guesse",a)
            break;

                    
                
        
    

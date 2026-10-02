l=[    1,"|",2,"|",3   ,
   "-----",
     4,"|",5,"|",6   ,
 "-----",
     7,"|",8,"|",9   ]
def dis(l):
    for j in range(17):
        if j<=4:
            print(l[j],end='')
        elif j>5 and j<11:
            print(l[j],end='')
        elif j==5 or j==11:
            print()
            print(l[j])
        else:
            print(l[j],end='')
dis(l)
print("\nPlayer 1 is X and Player 2 is O")
for i in range(9):
    if i%2==0:
        print("Player 1's turn")
        n=int(input("Enter no where you want to place X:"))
        if n not in l:
            print("Enter correct  place")
            i-=1
        else:
            for k in l:
                if k==n:
                    l[l.index(k)]="X"
                    break;
        dis(l)
        
                    
            
    else:
        print("\nPlayer 2's turn")
        n=int(input("Enter no where you want to place O:"))
        if n not in l:
            print("Enter correct  place")
            i-=1
        else:
            for k in l:
                if k==n:
                    l[l.index(k)]="O"
                    break;
        dis(l)
    c=0
    if l.count("X")>=3:
        if l[0]==l[2]==l[4]=="X" :
            c+=1
        elif l[0]==l[6]==l[12]=="X":
            c+=1
        elif l[2]==l[8]==l[14]=="X":
            c+=1
        elif l[4]==l[10]==l[16]=="X":
            c+=1
        elif l[6]==l[8]==l[10]=="X":
            c+=1
        elif l[12]==l[14]==l[16]=="X":
            c+=1
        elif l[0]==l[8]==l[16]=="X":
            c+=1
        elif l[4]==l[8]==l[12]=="X":
            c+=1

    if l.count("O")>=3:
        if l[0]==l[2]==l[4]=="O" :
            c+=2
        elif l[0]==l[6]==l[12]=="O":
            c+=2
        elif l[2]==l[8]==l[14]=="O":
            c+=2
        elif l[4]==l[10]==l[16]=="O":
            c+=2
        elif l[6]==l[8]==l[10]=="O":
            c+=2
        elif l[12]==l[14]==l[16]=="O":
            c+=2
        elif l[0]==l[8]==l[16]=="O":
            c+=2
        elif l[4]==l[8]==l[12]=="O":
            c+=2
    if c==1:
        print("\nCongrats Player 1 Wins")
        break;
    elif c==2:
        print("\nCongrats Player 2 Wins")
        break;
    elif c==0 and i==8:
        print("No one Wins")
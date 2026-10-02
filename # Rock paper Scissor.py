# Rock paper Scissor

while True:
    import random
    a=random.randint(1,10)
    if a>0 and a<3:
        ch="R"
    elif a>=3 and a<6:
        ch="P"
    else:
        ch="S"
    u=input("Enter Rock(R)\nPaper(P)\nSiccor(S)\n")
    if u==ch:
        print("same choice chose again")
    else:
        if ch=="R" and u=="S":
            print("YOU LOOSE",)
        elif ch=="R" and u=="P":
            print("YOU WIN")
        elif ch=="S" and u=="P":
            print("YOU LOOSE")
        elif ch=="S" and u=="R":
            print("YOU WIN")
        elif ch=="P" and u=="S":
            print("YOU WIN")
        else:
            print("YOU LOOSE")
        y=input("DO you want to continue")
        if y=="N" or y=="n":
            break;


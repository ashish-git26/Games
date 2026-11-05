c=1
s=1
l=["11"]
a="" 
n=int(input())
r=0
for i in range(n):
    for j in l:
        for k in j:
            t=j.count(k)
            a=a+str(k)+str(t)
        l.pop()
        l.append(a)
print(l)
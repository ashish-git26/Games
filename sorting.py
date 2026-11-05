n=int(input("Enter no of elements:"))
l=[]
for i in range(n):
    a=int(input("Enter number:"))
    l.append(a)
print("Original list=",l)
for j in range(n):
    for k in range(j+1,n):
        if l[j]>l[k]:
            temp=l[j]
            l[j]=l[k]
            l[k]=temp
print("Sorted List=",l)
            
    

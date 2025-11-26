c=int(input("Enter the size of list : "))
l1=[]
for i in range(c):
    d=int(input("Enter the no. : "))
    l1.append(d)
a=set()
b=set()
for i in l1:
    if i in a:
        b.add(i)
    else:
        a.add(i) 
print("The common elements are ",b)
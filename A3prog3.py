a=[]
b=[]
r=[]
d=int(input("Enter the size of a : "))
e=int(input("Enter the size of b : "))
s=0
c=0
for i in range(d):
    f=int(input("Enter the number for a : "))
    a.append(f)
    r.append(f)
for i in range(e):
    g=int(input("Enter the number for b : "))
    b.append(g)
    r.append(g)

r.sort()
for i in r:
    print(i)
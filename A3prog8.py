l1=[1,2,3,4]
l2=[5,6,7,8]
a=set()
b=set()
for i in l1:
    a.add(i)
for i in l2:
    b.add(i)
a=a.intersection(b)
if not a:
    print("No Common")
else:
    print("Has Common")
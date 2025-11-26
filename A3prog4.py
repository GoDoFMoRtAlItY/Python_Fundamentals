a=(1,2,3,4,5,6)
b=()
c=()
e=0
f=0
for i in a:
    if(i%2==0):
        b+=(i,)
    else:
        c+=(i,)
print("Even : ")
for i in b:
    print(i)
print("Odd : ")
for i in c:
    print(i)
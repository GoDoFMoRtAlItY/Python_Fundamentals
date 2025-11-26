a=[]
s=0
c=0
for i in range(0,6):
    b=int(input("Enter the number : "))
    a.insert(i,b)
for i in range(0,6):
    s+=a[i]
    c+=1
print("The average is : ",s/c)
a=int(input("Enter a number : "))
c=0
while (a!=0) : 
    b=int(a%10)
    a=int(a/10)
    c+=1
print(c," digit number")
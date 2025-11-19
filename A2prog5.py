a=int(input("Enter a number : "))
b=0
while (a!=0) : 
    b+=int(a%10)
    a=int(a/10)
print("sum : ",b)
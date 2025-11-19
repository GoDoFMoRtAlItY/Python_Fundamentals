def is_prime(n) :
    c=0
    for i in range(2,n+1): 
        if(n%i==0):
            c+=1
    if(c==1):
        return ("true")
    else:
        return ("false")
n=int(input("Enter a number : "))
print(is_prime(n))
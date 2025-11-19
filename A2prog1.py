a=int(input("Enter salary : "))
if(a<30000) :
    print("Your tax is : ",a*0.05)
elif(a>=30000 and a<=70000) : 
    print("Your tax is : ",a*0.15)
elif(a>=30000 and a<=70000) : 
    print("Your tax is : ",a*0.25)
else :
    print("Invalid")
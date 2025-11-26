a=input("Enter a word : ")
b=""
for ch in a :
    b=ch+b
if(a==b):
    print("palindrome")
else :
    print("Non Palindrome")
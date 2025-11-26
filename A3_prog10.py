c=input("Enter a string : ")
a=set()
b=set()
d=0
for i in c:
    if i in a:
        b.add(i)
    else:
        a.add(i)
        d+=1
print("All unique characters are : ",a)
print("Count of all unique characters are : ",d)
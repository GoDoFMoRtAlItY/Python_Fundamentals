words=["apple","banana","kiwi","cherry","mango"]
fruit={}
for i in words :
    name=i
    size=len(i)
    fruit.update(
        {name:size}
    )
print(fruit.items())

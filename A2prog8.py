def calculator(a,b,operation) :
    match operation:
        case "+":
            print (a+b)
        case "-":
            print (a-b)
        case "*":
            print (a*b)
        case "/":
            print (a/b)
        case _:
            print("invalid")
a=int(input("Enter the first no. : "))
b=int(input("Enter the second no. : "))
operation=input("Enter the operator sign : ")
calculator(a,b,operation)
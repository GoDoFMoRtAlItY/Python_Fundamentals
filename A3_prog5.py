b={}
while(1):
    print("A : Add a student")
    print("B : Update marks")
    print("C : Search for a student")
    print("D : Display all students and marks")
    a=input("Enter the input : ")
    match a:
        case "A" :
            c=input("Enter the Student name : ")
            d=input("Enter the student marks : ")
            b.update(
                {c : d}
            )
        case "C" :
            e=input("Enter the Student name : ")
            f=b.get(e)
            print(f)
        case "D":
            print(b.items())
        case _:
            break;
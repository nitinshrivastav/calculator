def calculator():
    a = int(input("enter 1st number:"))
    b = int(input("enter 2nd number:"))
    print("select a choice:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice=int(input("select a choice:"))
    if(choice==1):
        print(a+b)

    elif(choice==2):
        print(a-b)

    elif(choice==3):
        print(a*b)
    
    elif(choice==4):
        print(a/b)

    else :
        print("invalid choice")

calculator()
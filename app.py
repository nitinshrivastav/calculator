def calculator():
    x=int(input("enter a number"))
    z=int(input("enter a number"))
    print("press 1 for (+)")
    print("press 2 for (-)")
    print("press 3 for (/)")
    print("press 4 for (*)")
    a=int(input("enter your choice"))
    if(a==1):
        x+z
    elif(a==2):
        x-z
    elif(a==3):
        x/z
    else:
        x*z
calculator()

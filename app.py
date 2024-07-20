from db import db
def calculator():
    
    a= int(input('enter a number'))
    b= int(input('enter a number'))
    print('press 1 for addition')
    print('press 2 for sub')
    print('press  3for mul')
    print('press 4 for div')
    c= input('enter your choice')
    if(c=='1'):
        s='+'
        r=a+b
    elif(c=='2'):
        s='-'
        r=a-b
    elif(c=='3'):
        s='*'
        r=a*b
    elif(c=='4'):
        s='/'
        r=a/b
    else:
        s='@'
        print("invalid choice")
    db(a,b,s,r)
calculator()




    
    
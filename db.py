import mysql.connector
def db(n1,n2,sym,res):
    
    database = mysql.connector.connect(host='localhost',user='root',password='1234567890')
    box=database.cursor()
    try:
        box.execute('create database abc')
        box.execute('use abc')
    except:
        box.execute('use abc')
    try:
         box.execute('create table calculation(num1 int,num2 int,choice varchar(1),ans int)')
    except:
        print('table is already created')
    q='insert into calculation values(%s,%s,%s,%s)'
    data=(n1,n2,sym,res)
    box.execute(q,data)
    database.commit()
    database.close()        
    print("Data has been added")

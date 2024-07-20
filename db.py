import mysql.connector
def db():
    database= mysql.connector.connect(host="localhost",user="root",password="000001")
    box=database.cursor()   
    try:
        box.execute("creat database xyz")
        box.execute("use xyz")
        box.execute("insert into xyz")

    
            

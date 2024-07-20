import mysql.connector
def db(n1,n2,sym,res):
    data = mysql.connector.connect(host="localhost",user="root",password="7011581376")
    box = data.cursor()
    try:
      box.execute("create database shiv")
      box.execute("use shiv")
    except:
       box.execute("use shiv")
    try:
       box.execute("create table skb(num1 int, num2 int, choice int, result int)")
    except:
       print("table already exists")
    q = "insert into skb values(%s,%s,%s,%s)"
    val=(n1,n2,sym,res)
    box.execute(q,val)
    data.commit()
    data.close()
    print("data added")
      
      



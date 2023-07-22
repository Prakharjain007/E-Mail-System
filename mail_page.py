from mysql_connection import mysql_connection 
import datetime
from tabulate import tabulate

def mail_page(uname):
    print("1. Compose")
    print("2. Check Sent ")
    print("3. Inbox")
    print("4. Change Password")
    print("5. Logout") 

    choice= input("What do you want to perform: ")
    print("\n--------------------------------------------\n")
    
    if(choice=="1"):
        compose(uname)
    elif(choice=='2'):
        sent()
    elif(choice=="3"):
        inbox()
    elif(choice=="4"):
        cgpswd()
    elif(choice == "5"):
        return 
    else:
        print("Wrong Input!!! ")
        print("Try Again")
    
    mail_page(uname)

def compose(uname):
    mycon,cur = mysql_connection()
    reciver_mail= input("Enter Reciever's Mail ID: ")
    reciver_mail = reciver_mail.lower()
    sub= input("Enter Subject of the Mail: ")
    text=input("Enter the mail text: ")
    print("\n--------------------------------------------\n")
    date=datetime.date.today()
    
    sql= 'select * from login'
    cur.execute(sql)
    result= cur.fetchall() 
    exists = False
    for row in result:
        if(row[2] == reciver_mail):
            exists = True
            break

    else:
        print("Username doesn't Exists, Enter a valid username")
        print("\n--------------------------------------------\n")

    if(exists == True):
        try:
            sql='Insert into mails (mail_date,sender,receiver,subject,text) values(%s,%s,%s,%s,%s)'
            data=[date,uname,reciver_mail,sub,text]
            cur.execute(sql,data)
            mycon.commit()

        except:
            print("Something is Wrong!!!!")
            print("\n--------------------------------------------\n")
        else:
            print("Mail Sent Successfully")
            print("\n--------------------------------------------\n")

def sent(uname):
    mycon,cur=mysql_connection()
    sql='select * from mails'
    cur.execute(sql)
    result = cur.fetchall()
    mails=[]
    for row in result:
        if row[2]==uname:
            mails.append(row)

    if(len(mails)==0):
        print("No Sent Mails")
        print("\n--------------------------------------------\n")

    else:
        print("\n--------------------------------------------\n")
        keys=["Serial No.","Date","Sender","Reciever","Subject","Mail"]
        print(tabulate(mails, headers = keys, tablefmt = 'pretty', showindex = False))
        print("\n--------------------------------------------\n")

    
def inbox(uname):
    mycon,cur=mysql_connection()
    sql='select * from mails'
    cur.execute(sql)
    result = cur.fetchall()
    mails=[]
    for row in result:
        if row[3]==uname:
            mails.append(row)

    if(len(mails)==0):
        print("No Recieved Mails")
        print("\n--------------------------------------------\n")

    else:
        print("\n--------------------------------------------\n")
        keys=["Serial No.","Date","Sender","Reciever","Subject","Mail"]
        print(tabulate(mails, headers = keys, tablefmt = 'pretty', showindex = False))
        print("\n--------------------------------------------\n")
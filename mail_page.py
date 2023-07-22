from mysql_connection import mysql_connection 
import datetime


def mail_page(uname):

    while(True):
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


def compose(uname):
    mycon,cur = mysql_connection()
    reciver_mail= input("Enter Reciever's Mail ID: ")
<<<<<<< HEAD
    sub= input("Enter Subject of the Mail: ")
    text=input("Enter the mail text: ")
    print("\n--------------------------------------------\n")
    date=datetime.date.today()
    sql='Insert into mails (mail_date,sender,receiver,subject,text) values(%s,%s,%s,%s,%s)'
    data=[date,uname,reciver_mail,sub,text]
    try:

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
    sql='selct * from mails'
    result = cur.fetchall()

    



=======
    sub= input("Enter Subject of the MailL: ")
    text=input("Enter the Mail Text: ")
    sql='Insert into mails values(%s,%s,%s)'
    data=[uname,reciver_mail,sub,text]
    cur.execute(sql,data)
    mycon.commit()
>>>>>>> eaf69e5397c5f060b612c4d28301ec228b9432ee

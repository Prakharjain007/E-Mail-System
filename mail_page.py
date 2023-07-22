from mysql_connection import mysql_connection 



def mail_page(uname):

    while(True):
        print("1. Compose")
        print("2. Check Sent ")
        print("3. Inbox")
        print("4. Change Password")
        print("5. Logout")

        choice= input("What do you want to perform")
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
    reciver_mail= input("Enter Reciever's Mail ID")
    sub= input("Enter Subject of the Mail")
    text=input("Enter the mail text")
    sql='Insert into mails values(%s,%s,%s)'
    data=[uname,reciver_mail,sub,text]
    cur.execute(sql,data)
    mycon.commit()
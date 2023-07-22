from mysql_connection import mysql_connection
import maskpass
from mail_page import mail_page

def login():
    mycon,cur=mysql_connection()
    uname=input("Enter Your Username: ")
    pswd=maskpass.askpass(prompt="Enter your Password: ",mask="*")
    print("\n--------------------------------------------\n")

    sql= 'select * from login'

    cur.execute(sql)
    result= cur.fetchall()
    while(True):
        success = False
        for row in result:
            if row[2] == uname and row[3] ==  pswd:
                print("Login Successfull")
                print("\n--------------------------------------------\n")
                mail_page(uname)
                success= True
                return
        
        if(success == False):
            print("Username or Password is Incorrect")
            print("\n--------------------------------------------\n")
        
        while(True):
            choice= input("Do you want to login?[y/n] ")
            print("\n--------------------------------------------\n")
            if(choice.lower()=='y'):
                login()
                return
            
            elif(choice.lower()=='n'):
                return
            
            else:

                print("Wrong Input Try Again!!!")
                print("\n--------------------------------------------\n")

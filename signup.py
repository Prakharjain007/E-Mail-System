import maskpass
from mysql_connection import mysql_connection 
from login import login   

def signup():
    mycon,cur = mysql_connection()
    fname=input("Enter Your First Name: ")
    lname=input("Enter Your Last  Name: ")
    print("\n--------------------------------------------\n")
    print("Your username should contain '@'")
    uname=input("Enter Your Username: ")
    pswd=maskpass.askpass(prompt="Enter your Password: ",mask="*")
    print("\n--------------------------------------------\n")

    sql='insert into login values(%s,%s,%s,%s)'
    data = [fname,lname,uname,pswd]
    
    try:
        cur.execute(sql,data)
        mycon.commit()
    except:
        print("Something Went Wrong")
        print("\n--------------------------------------------\n")
        return 

    else:
        print("Signup was Successfull")
        print("\n--------------------------------------------\n")
    
    while(True):
        choice= input("Do you want to login [y/n]: ")
        print("\n--------------------------------------------\n")
        if(choice.lower()=='y'):
            login()
            return
        elif(choice.lower()=='n'):
            return
        else:
            print("Wrong Input Try Again!!!")
            print("\n--------------------------------------------\n")
            


    

   

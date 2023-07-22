import maskpass
from mysql_connection import mysql_connection 
from login import login   

def signup():
    mycon,cur = mysql_connection()

    while(True):
        fname=input("Enter Your First Name: ")
        lname=input("Enter Your Last  Name: ")
        print("\n--------------------------------------------\n")
        print("Your Username must contain '@'")
        uname=input("Enter Your Username: ")
        print("\n--------------------------------------------\n") 
        print("Your Password must contain a Number")
        pswd=maskpass.askpass(prompt="Enter your Password: ",mask="*")
        print("\n--------------------------------------------\n") 

        pass_val = password_validation(pswd)
        user_val = username_validation(uname)
        
        if(pass_val != True or user_val != True):
            print("Password or Username is/are not Valid")
            print("\n--------------------------------------------\n")
            
            while(True):
                choice= input("Do you want to Signup again?[y/n] ")
                print("\n--------------------------------------------\n")
                if(choice.lower()=='y'):
                    signup()
                    return
                
                elif(choice.lower()=='n'):
                    return
                
                else:
                    print("Wrong Input Try Again!!!")
                    print("\n--------------------------------------------\n")

        else:
            break

    
    try:
        sql='insert into login values(%s,%s,%s,%s)'
        data = [fname,lname,uname,pswd]
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
        
def password_validation(pswd):

    num = '123456789'
    for letter in pswd:
        if (letter in num):
            return True
    else:
        return False
    
def username_validation(uname):

    if('@' in uname):
        return True
    
    else:
        return False


    





    

   

from signup import signup
from login import login

print("\n--------------------------------------------\n")
def main():
    print("Welcome to Email")
    print("\n--------------------------------------------\n")
    
    print("1. Signup")
    print("2. Login")
    print("3. Exit")
    ch = input("Login as: ")
    print("\n--------------------------------------------\n")
    
    if(ch == "1"):
        signup()

    elif(ch == "2"):
        login()
       
    elif(ch == "3"):
        print("Thank you for using Email")
        print("Have a Nice Day")
        print("\n--------------------------------------------")
        return
        
    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")
        
    main()
    
if __name__ == "__main__":
    main()
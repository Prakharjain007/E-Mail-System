import mysql.connector as ms
from cred.Cred import Cred

def mysql_connection():
    password,db =  Cred() 
    mycon=ms.connect(host="localhost",user="root",db=db,passwd=password)
    cur=mycon.cursor()
    return mycon,cur
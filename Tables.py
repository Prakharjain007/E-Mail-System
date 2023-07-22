from cred.Cred import Cred
import mysql.connector as ms
from mysql_connection import mysql_connection

def logintable(mycon,cur):
    sql='''
    create table login(
    first_name varchar(50) Not Null,
    last_name varchar(50),
    username varchar(50) primary key,
    password varchar(50)
    )
    '''
    cur.execute(sql)
    mycon.commit()

def email(mycon,cur):
    sql ='''
    create table mails(
    s_no int primary key auto_increment,
    mail_date varchar(10) not null,
    sender varchar(50) not null,
    receiver varchar(50) not null,
    subject varchar(50),
    text varchar(500)
    ) 
    '''
    cur.execute(sql)
    mycon.commit()


def main():
    mycon,cur = mysql_connection()
    logintable(mycon,cur)
    email(mycon,cur)
    print("Table Created Successfully")
    

if(__name__ == "__main__"):
    main()
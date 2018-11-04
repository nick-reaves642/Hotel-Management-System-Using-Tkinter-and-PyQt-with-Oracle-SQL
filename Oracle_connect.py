import getpass
import cx_Oracle
def connect():
    print('Enter username password to connect to the oracle database...')
    username=str(input('Username: '))
    con=cx_Oracle.connect(username+'/'+str(getpass.getpass())+'@localhost/orcl')
    cur=con.cursor()
    return (cur,con)

if __name__=='__main__':
    connect()
    
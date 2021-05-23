'''
import pyodbc

# Define the server and the database
server = 'DESKTOP-H8E5RPI\\NNKNSQL'
database = 'LibraryDB'

# Define the connection string
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server}; \
    SERVER='+ server +'; \
    DATABASE='+ database +';\
    Trusted_Connection=yes;'
)

# Create the Cursor
cursor = cnxn.cursor()

cursor.execute('SELECT * from BOOKS')
for row in cursor:
    print(row)

cursor.close()
cnxn.close()

'''

#cursor.execute('CREATE TABLE ADMINS ([Usernames] varchar(20) PRIMARY KEY,[Password] varchar(20))')
#cursor.execute('''CREATE TABLE USERS(
#	[Usernames] varchar(20) PRIMARY KEY,
#	[Passwords] varchar(20)
#)''')
#cursor.execute('''CREATE TABLE BOOKS(
#	[Book_ID] char(5) PRIMARY KEY,
#	[Book_name] nvarchar(50),
#	[Author] nvarchar(50),
#	[Book_type] varchar(30),
#	[Book_format] char(5),
#	[Book_link] varchar(50)
#)''')

import sqlite3

'''
connection = sqlite3.connect('LibraryDB')
cursor = connection.cursor()

sql_file = open('Library.sql')
sql_as_string = sql_file.read()
sql_as_string = sql_as_string.replace("\n", " ")

cursor.executescript(sql_as_string)

for row in cursor.execute("SELECT * FROM BOOKS"):
    print(row)

connection.close()
'''

import socket
import threading
import SignInUp
import Search
PORT = 80

connection = sqlite3.connect('LibraryDB')
cursor = connection.cursor()

def on_new_client(client):
    while True:
        message = client.recv(1024).decode('1024')
        if message == 'SIGNIN':
            SignInUp.sign_in_click(client,cursor)
        elif message =='SIGNUP':
            SignInUp.sign_up_click(client,cursor)
        elif message == 'SEARCH':
            Search.search_click(client,cursor)



serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("", PORT))
serverSocket.listen(5)
print("Waiting for connection...")

while True:
   client, addr = serverSocket.accept()     # Establish connection with client.
   thread_client = threading.Thread(target=on_new_client,args=(client))
   thread_client.start()

s.close()

    

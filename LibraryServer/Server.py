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
sql_as_string = sql_as_string.replace('\n', ' ')

cursor.executescript(sql_as_string)

for row in cursor.execute('SELECT * FROM BOOKS'):
    print(row)

connection.close()
'''

import socket
import tkinter as tk
from tkinter import messagebox
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
        elif message == 't':
            continue

#99cc66
#669966
serverSocket = None
class ServerLogin():
    def __init__(self,root):
            self.root=root
            self.root.title('ONLINE LIBRARY ADMIN')
            self.root.geometry('1080x607+100+50')
            self.root.config(bg='#99cc66')
            self.root.resizable(False,False)
            self.root.grab_set()
            self.create_widgets()


    def create_widgets(self):
        self.Login_label = tk.Label(self.root, width=35, height=4, text='Library manage system', font=('Elephant', 32, 'bold'), bg='#FFCC00', fg = '#0066CC')
        self.Login_label.place(x=0, y=0)

        self.frame=tk.Frame(self.root,)
        self.frame.place(x=340,y=170,width=400,height=450)

        self.user_label=tk.Label(self.frame,text='USERNAME',font=('Andalus',11),fg='black')
        self.user_label.place(x=80,y=70)

        self.user_entry = tk.Entry(self.frame,font=('times new roman',14))
        self.user_entry.place(x=80,y=100,width=250)

        self.pass_label = tk.Label(self.frame, text='PASSWORD', font=('Andalus', 11),fg='black')
        self.pass_label.place(x=80, y=150)

        self.pass_entry = tk.Entry(self.frame,show='*', font=('times new roman', 14))
        self.pass_entry.place(x=80, y=180,width=250)

        self.signin_but=tk.Button(self.frame,text='Login',bg='#0099FF',activebackground='#0066FF',activeforeground='white',fg='white',font=('Arial Rounded MT Bold',15,'bold'),cursor='hand2',command=lambda:self.admin_signin())
        self.signin_but.place(x=80,y=230,height=35,width=250)

    def admin_signin(self):
        if self.user_entry.get() == '':
            messagebox.showwarning('Warning', 'Please Enter Username.')
        elif self.pass_entry.get()  == '':
            messagebox.showwarning('Warning', 'Please Enter Password.')
        else:
            connection = sqlite3.connect('LibraryDB')
            cursor = connection.cursor()
            user = self.user_entry.get()
            password = self.pass_entry.get() 
            s = SignInUp.admin_sign_in(cursor,user,password)
            if s == 'Error':
                messagebox.showwarning('Warning', 'The username or password is incorrect.')
            else:
                connection.commit()
                connection.close()
                self.root.withdraw()
                root = tk.Toplevel()
                sp = ServerProcess(root)
                root.mainloop()


                
class ServerProcess():    
    def __init__(self,root):
        self.root=root
        self.my_clients = []
        self.root.title('ONLINE LIBRARY SERVER')
        self.root.geometry('720x560+200+100')
        self.root.config(bg='#99cc66')
        self.root.resizable(False,False)
        self.root.grab_set()
        self.create_widgets()  

    def create_widgets(self):
        self.Login_label = tk.Label(self.root, width=30, height=3, text='Library manage system', font=('Elephant', 25, 'bold'), bg='#FFCC00', fg = '#0066CC')
        self.Login_label.place(x=0, y=0)

        self.frame=tk.Frame(self.root)
        self.frame.place(x=170,y=120,width=380,height=400)

        self.open_but = tk.Button(self.root,text='Open Server',bg='#0099FF',activebackground='#0066FF',activeforeground='white',fg='white',font=('Arial Rounded MT Bold',15,'bold'), command=lambda:self.connect_click())
        self.open_but.place(x=240,y=210,height=90,width=240)

        self.open_but = tk.Button(self.root,text='Disconnect All',bg='#FF3366',activebackground='#CC3366',activeforeground='white',fg='white',font=('Arial Rounded MT Bold',15,'bold'), command=lambda:self.disconnect_click())
        self.open_but.place(x=240,y=320,height=90,width=240)

    def send_all_clients(self,message):
        for client in self.my_clients:
            client.send(message)

    def disconnect_click(self):
        global serverSocket
        MsgBox = tk.messagebox.askquestion ('Disconnect','Are you sure you want to disconnect all client',icon = 'warning')
        if MsgBox== 'yes':
            s = 'QUIT'
            self.send_all_clients(s)
            serverSocket.close()
        else:
             tk.messagebox.showinfo('Return','You will now return to the application screen')



        

         

        

        




root = tk.Tk()
app = ServerLogin(root)
root.mainloop()
'''
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', PORT))
serverSocket.listen(5)
print('Waiting for connection...')

while True:
   client, addr = serverSocket.accept()     # Establish connection with client.
   thread_client = threading.Thread(target=on_new_client,args=(client))
   thread_client.start()

s.close()
'''
    

import socket
import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
import threading
import SignInUp
import Search
import View

PORT = 80
'''
connection = sqlite3.connect('LibraryDB')
cursor = connection.cursor()

sql_file = open('Library.sql')
sql_as_string = sql_file.read()
sql_as_string = sql_as_string.replace('\n', ' ')

cursor.executescript(sql_as_string)

for row in cursor.execute('SELECT * FROM BOOKS'):
    print(row)

connection.commit()
connection.close()
'''

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
class Server_login_GUI():
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
                sp = Server_control(root)
                root.mainloop()

        
class Server_control():    
    def __init__(self,root):
        self.root=root
        self.my_clients = []
        self.server_socket = None
        self.connection = sqlite3.connect('LibraryDB')
        self.cursor = self.connection.cursor()
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

        self.open_but = tk.Button(self.root,text='Open Server',bg='#0099FF',activebackground='#0066FF',activeforeground='white',fg='white',font=('Arial Rounded MT Bold',15,'bold'), command=lambda:self.open_click())
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
    
    def open_click(self):
        self.max_clients = askstring('Max clients', 'What is the maximum number of clients you want to connect to?')
        try:
            self.server_socket.bind(("", PORT))
            serverSocket.listen(5)
        except socket.error as e:
            print(str(e))

        print('Waiting for connection...')
        while True:
            client, addr = self.server_socket.accept()
            if len(self.my_clients) >= self.max_clients:
                client.send("The library is overloaded".encode('utf-8'))
                client.close()
                continue
            client.send("Welcome to the library".encode('utf-8'))
            self.max_clients += [client]
            new_thread = threading.Thread(lambda:self.thread_client(client))
            new_thread.daemon = True
            new_thread.start()

    def thread_client(self,client):
        while True:
            message = client.recv(1024).encode('utf-8')
            if message == 'SIGNIN':
                SignInUp.sign_in_click(client,self.cursor)
            elif message == 'SIGNUP':
                SignInUp.SignInUp.sign_up_click(client,self.cursor)
                connection.commit()
            elif message == 'SEARCH':
                Search.search_click(client,self.cursor)
            elif message == 'VIEW':
                View.view_click(client,self.cursor)
            elif message == 'DOWNLOAD':
                View.view_click(client,self.cursor)
            elif message == 'SIGNOUT':
                self.my_clients.remove(client)
                client.close()
            else:
                break
                
root = tk.Tk()
app = Server_login_GUI(root)
root.mainloop()
        

import json

def sign_in(cursor,username, password):
    cursor.execute('SELECT * FROM USERS WHERE Username="' + username + '" AND Password="' + password + '"')
    if cursor.fetchall()==[]:
        return 'Incorrect email address or password'
    else:
        return 'Success'

def sign_up(cursor,username, password):
    cursor.execute('SELECT * FROM USERS WHERE Username="' + username + '"')
    if cursor.fetchall() == []:
        try:
            cursor.execute('INSERT INTO USERS VALUES("'+username+'","' + password + '")')
            return 'Success'
        except:
            return 'Error'
    else:
        return 'Account Exists'

def admin_sign_in(cursor,username,password):
    cursor.execute('SELECT * FROM ADMINS WHERE Username="' + username + '" AND Password="' + password + '"')
    if cursor.fetchall()==[]:
        return 'Error'
    else:
        return 'Success'


def sign_in_click(client, currsor):
    info = client.recv(1024)
    info = json.loads(info.decode("utf-8"))
    s = sign_in(currsor,info[0],info[1])
    client.send(s)

def sign_up_click(client,cursor):
    info = client.recv(1024)
    info = json.loads(info.decode("utf-8"))
    s = sign_up(cursor,info[0],info[1])
    client.send(s)

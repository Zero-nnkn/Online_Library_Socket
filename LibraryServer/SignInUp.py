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

def sign_in(cursor,username, password):
    cursor.execute('SELECT * FROM USERS WHERE Username="' + username + '" AND Password=' + password + '"')
    if cursor.fetchall()==[]:
        return 'Incorrect email address or password'
    else:
        return 'Success'

        
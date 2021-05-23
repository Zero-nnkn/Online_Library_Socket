import json

def serch_by_id(cursor,book_id):
    cursor.execute('SELECT Book_ID, Book_name, Author, Book_type, Book_format FROM BOOKS WHERE Book_ID LIKE "%' + book_id + '%"')
    return cursor.fetchall()

def serch_by_name(cursor,book_name):
    cursor.execute('SELECT Book_ID, Book_name, Author, Book_type, Book_format FROM BOOKS WHERE Book_name LIKE "%' + book_name + '%"')
    return cursor.fetchall()

def serch_by_type(cursor,book_type):
    cursor.execute('SELECT Book_ID, Book_name, Author, Book_type, Book_format FROM BOOKS WHERE Book_type LIKE "%' + book_type + '%"')
    return cursor.fetchall()

def serch_by_author(cursor,book_author):
    cursor.execute('SELECT Book_ID, Book_name, Author, Book_type, Book_format FROM BOOKS WHERE Author LIKE "%' + book_author + '%"')
    return cursor.fetchall()

def serch_choice(cursor, searchString):
    search_by = searchString[:searchString.find(' ')]
    if search_by == 'F_ID':
        result = serch_by_id(cursor,searchString[searchString.find(' ')+1:])
    elif search_by == 'F_Name':
        result = serch_by_name(cursor,searchString[searchString.find(' ')+1:])
    elif search_by == 'F_Type':
        result = serch_by_type(cursor,searchString[searchString.find(' ')+1:])
    elif search_by == 'F_Author':
        result = serch_by_author(cursor,searchString[searchString.find(' ')+1:])
    else:
        result = []
    return result

def search_click(client,cursor):
    while True:
        buffer = client.recv(1024).decode('utf-8')
        if buffer=='searchString':
            searchString = client.recv(1024).decode('utf-8')
            s = serch_choice(cursor,searchString)
            dataToSend = json.dumps(s).encode('utf-8') 
            client.send(dataToSend)
        else:
            break

    
def view_book(cursor,book_id):
    cursor.execute('SELECT Book_link FROM BOOKS WHERE Book_ID LIKE "%' + book_id + '%"')
    return cursor.fetchall()[0][0]

def view_click(client, cursor):
    book_id = client.recv(1024).decode('utf-8')
    book_link = view_book(cursor,book_id)
    f = open(book_link,'rb')
    l = f.read(1024)
    while(l):
        client.send(l)
        l = f.read(1024)
    f.close()

def recv(clientSocket):
    with open('rec_file.txt', 'wb') as f:
        while True:
            data = clientSocket.recv(1024)
            if not data:
                break
            f.write(data)




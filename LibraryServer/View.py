def view_book(cursor,book_id):
    cursor.execute('SELECT Book_link FROM BOOKS WHERE Book_ID LIKE "%' + book_id + '%"')
    return cursor.fetchall()[0][0]


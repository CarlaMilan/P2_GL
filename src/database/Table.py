'''CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR UNIQUE,
    password_hash VARCHAR
    )
    '''
    
'''
    CREATE TABLE IF NOT EXISTS fav_books(
    fav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id VARCHAR,
    book_id VARCHAR ,
    UNIQUE(user_id, book_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(book_id) REFERENCES books(book_id)
    )
    '''
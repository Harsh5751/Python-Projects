import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookTable (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

#connect always run when calling this script in the import statement of BookStore
connect()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    #put NULL for value of id as python will automatically assign that
    curr.execute("INSERT INTO bookTable VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM bookTable")
    rows = curr.fetchall()
    conn.close()
    return rows

#pass default values as empty string so user can only search by only one of there parameters
def search(title = "", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM bookTable WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    rows = curr.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("DELETE FROM bookTable WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("UPDATE bookTable SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


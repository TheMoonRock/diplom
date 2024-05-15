import sqlite3

db = sqlite3.connect('itsql.db')

c = db.cursor()

c.execute("""CREATE TABLE articles
    title text,
    full_text text,
    views integer,
    avtor text
""")

db.commit()

db.close()

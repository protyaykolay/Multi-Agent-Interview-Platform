import sqlite3

def get_results():

    conn=sqlite3.connect("database.db")

    cursor=conn.cursor()

    cursor.execute(

"SELECT * FROM candidate"

)

    data=cursor.fetchall()

    conn.close()

    return data
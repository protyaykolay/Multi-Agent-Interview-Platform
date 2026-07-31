import sqlite3

from datetime import datetime

def save_result(

name,

email,

student_id,

score

):

    conn=sqlite3.connect("database.db")

    cursor=conn.cursor()

    cursor.execute(

"""

INSERT INTO candidate(

name,

email,

student_id,

score,

date

)

VALUES(

?,?,?,?,?

)

""",

(

name,

email,

student_id,

score,

datetime.now()

)

)

    conn.commit()

    conn.close()
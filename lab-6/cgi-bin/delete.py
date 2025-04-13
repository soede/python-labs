#!/usr/bin/env python3
import sqlite3
import os
import cgi, cgitb
cgitb.enable()

print("Content-Type: text/html; charset=utf-8\n")
form = cgi.FieldStorage()
program_id = form.getvalue("id")
db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "software.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

if program_id:
    cursor.execute("DELETE FROM Programs WHERE id = ?", (program_id,))
    conn.commit()
    print("<html><body>")
    print("<p>Программа удалена!</p>")
    print("<p><a href='/cgi-bin/index.py'>Вернуться к списку</a></p>")
    print("</body></html>")
else:
    print("<html><body>")
    print("<p>ID программы не указан!</p>")
    print("<p><a href='/cgi-bin/index.py'>Вернуться к списку</a></p>")
    print("</body></html>")
conn.close()

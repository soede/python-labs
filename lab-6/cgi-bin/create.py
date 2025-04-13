#!/usr/bin/env python3
import sqlite3
import os
import cgi, cgitb
cgitb.enable()

print("Content-Type: text/html; charset=utf-8\n")
form = cgi.FieldStorage()
method = os.environ.get("REQUEST_METHOD", "GET")

db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "software.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

if method == "POST":
    name = form.getvalue("name")
    version = form.getvalue("version")
    license_type = form.getvalue("license_type")
    developer_id = form.getvalue("developer_id")
    if not developer_id:
        developer_id = None
    else:
        developer_id = int(developer_id)
    if name and version and license_type:
        cursor.execute("""
            INSERT INTO Programs (name, version, license_type, developer_id)
            VALUES (?, ?, ?, ?)
        """, (name, version, license_type, developer_id))
        conn.commit()
        print("<html><body>")
        print("<p>Программа успешно добавлена!</p>")
        print("<p><a href='/cgi-bin/index.py'>Вернуться к списку</a></p>")
        print("</body></html>")
    else:
        print("<html><body>")
        print("<p>Ошибка: заполните все обязательные поля!</p>")
        print("<p><a href='/cgi-bin/create.py'>Вернуться к форме</a></p>")
        print("</body></html>")
else:
    # GET-запрос – вывод формы
    cursor.execute("SELECT id, name FROM Developers")
    developers = cursor.fetchall()
    print("""
<html>
<head>
<meta charset="utf-8">
<title>Добавить программу</title>
<style>
  body { font-family: Arial, sans-serif; background: #f5f5f5; padding: 20px; }
  form { background: #fff; padding: 20px; border: 1px solid #ccc; max-width: 400px; margin: auto; }
  input, select { width: 100%; padding: 8px; margin: 5px 0 10px; }
  .button { padding: 10px 15px; border: none; background: #007BFF; color: #fff; cursor: pointer; }
</style>
</head>
<body>
<h1>Добавить программу</h1>
<form method="post" action="/cgi-bin/create.py">
  <label>Название:</label>
  <input type="text" name="name" required>
  <label>Версия:</label>
  <input type="text" name="version" required>
  <label>Тип лицензии:</label>
  <input type="text" name="license_type" required>
  <label>Разработчик:</label>
  <select name="developer_id">
      <option value="">-- Не выбран --</option>
    """)
    for dev in developers:
        print(f'<option value="{dev[0]}">{dev[1]}</option>')
    print("""
  </select>
  <input class="button" type="submit" value="Добавить">
</form>
<p style="text-align: center;"><a href="/cgi-bin/index.py">Вернуться к списку</a></p>
</body>
</html>
    """)
conn.close()

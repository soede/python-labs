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
    program_id = form.getvalue("id")
    name = form.getvalue("name")
    version = form.getvalue("version")
    license_type = form.getvalue("license_type")
    developer_id = form.getvalue("developer_id")
    if not developer_id:
        developer_id = None
    else:
        developer_id = int(developer_id)
    if program_id and name and version and license_type:
        cursor.execute("""
            UPDATE Programs
            SET name = ?, version = ?, license_type = ?, developer_id = ?
            WHERE id = ?
        """, (name, version, license_type, developer_id, program_id))
        conn.commit()
        print("<html><body>")
        print("<p>Программа успешно обновлена!</p>")
        print("<p><a href='/cgi-bin/index.py'>Вернуться к списку</a></p>")
        print("</body></html>")
    else:
        print("<html><body>")
        print("<p>Ошибка: заполните все обязательные поля!</p>")
        print("<p><a href='/cgi-bin/index.py'>Вернуться к списку</a></p>")
        print("</body></html>")
else:
    program_id = form.getvalue("id")
    if program_id:
        cursor.execute("SELECT id, name, version, license_type, developer_id FROM Programs WHERE id = ?", (program_id,))
        program = cursor.fetchone()
        if program:
            cursor.execute("SELECT id, name FROM Developers")
            developers = cursor.fetchall()
            print(f"""
<html>
<head>
<meta charset="utf-8">
<title>Обновить программу</title>
<style>
  body {{ font-family: Arial, sans-serif; background: #f5f5f5; padding: 20px; }}
  form {{ background: #fff; padding: 20px; border: 1px solid #ccc; max-width: 400px; margin: auto; }}
  input, select {{ width: 100%; padding: 8px; margin: 5px 0 10px; }}
  .button {{ padding: 10px 15px; border: none; background: #28a745; color: #fff; cursor: pointer; }}
</style>
</head>
<body>
<h1>Обновить программу</h1>
<form method="post" action="/cgi-bin/update.py">
  <input type="hidden" name="id" value="{program[0]}">
  <label>Название:</label>
  <input type="text" name="name" value="{program[1]}" required>
  <label>Версия:</label>
  <input type="text" name="version" value="{program[2]}" required>
  <label>Тип лицензии:</label>
  <input type="text" name="license_type" value="{program[3]}" required>
  <label>Разработчик:</label>
  <select name="developer_id">
    <option value="">-- Не выбран --</option>
            """)
            for dev in developers:
                selected = "selected" if program[4] == dev[0] else ""
                print(f'<option value="{dev[0]}" {selected}>{dev[1]}</option>')
            print("""
  </select>
  <input class="button" type="submit" value="Обновить">
</form>
<p style="text-align: center;"><a href="/cgi-bin/index.py">Вернуться к списку</a></p>
</body>
</html>
            """)
        else:
            print("<html><body>")
            print("<p>Программа не найдена!</p>")
            print("<p><a href='/cgi-bin/index.py'>Вернуться к списку</a></p>")
            print("</body></html>")
    else:
        print("<html><body>")
        print("<p>ID программы не указан!</p>")
        print("<p><a href='/cgi-bin/index.py'>Вернуться к списку</a></p>")
        print("</body></html>")
conn.close()

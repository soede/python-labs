#!/usr/bin/env python3
import sqlite3
import os

print("Content-Type: text/html; charset=utf-8\n")
print("""
<html>
<head>
<meta charset="utf-8">
<title>Список Программ</title>
<style>
  body { font-family: Arial, sans-serif; background: #f5f5f5; padding: 20px; }
  h1 { color: #333; }
  table { border-collapse: collapse; width: 100%; background: #fff; }
  th, td { border: 1px solid #ccc; padding: 10px; text-align: left; }
  th { background: #eee; }
  a { text-decoration: none; color: #007BFF; }
  a:hover { text-decoration: underline; }
  .button { padding: 5px 10px; border-radius: 3px; border: none; cursor: pointer; background: #007BFF; color: #fff; }
  .danger { background: #dc3545; }
</style>
</head>
<body>
<h1>Список Программ</h1>
<a class="button" href="/cgi-bin/create.py">Добавить программу</a>
<br/><br/>
""")

# Определяем путь к базе данных: файл находится на уровень выше (в корне проекта)
db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "software.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
SELECT Programs.id, Programs.name, Programs.version, Programs.license_type, Developers.name 
FROM Programs 
LEFT JOIN Developers ON Programs.developer_id = Developers.id
ORDER BY Programs.id
""")
rows = cursor.fetchall()

if rows:
    print("<table>")
    print("<tr><th>ID</th><th>Название</th><th>Версия</th><th>Лицензия</th><th>Разработчик</th><th>Действия</th></tr>")
    for row in rows:
        print(f"<tr>")
        print(f"<td>{row[0]}</td>")
        print(f"<td>{row[1]}</td>")
        print(f"<td>{row[2]}</td>")
        print(f"<td>{row[3]}</td>")
        print(f"<td>{row[4] if row[4] else 'N/A'}</td>")
        print(f"<td>"
              f"<a class='button' href='/cgi-bin/update.py?id={row[0]}'>Редактировать</a> "
              f"<a class='button danger' href='/cgi-bin/delete.py?id={row[0]}'>Удалить</a>"
              f"</td>")
        print(f"</tr>")
    print("</table>")
else:
    print("<p>Нет данных.</p>")

print("""
</body>
</html>
""")
conn.close()

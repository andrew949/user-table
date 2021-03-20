import sqlite3

conn = sqlite3.connect("d:/phiton/sqllite/table.sqlite")#таблица

c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'users'")

c.execute("""
CREATE table if not exists
    users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    );
""")

c.execute("""
CREATE table if not exists
    cars(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT UNIQUE,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
""")

# дополняем значения в таблицу пользователя
c.execute("""INSERT INTO users (name, email) VALUES ('Masha', 'masha@.com')""") 
c.execute("""INSERT INTO users (name, email) VALUES ('Serega', 'serega@.ru')""")
c.execute("""INSERT INTO users (name, email) VALUES ('Vasia', 'vasia@.ru')""")
c.execute("""INSERT INTO users (name, email) VALUES ('Petya', 'petya@.ru')""")
c.execute("""INSERT INTO users (name, email) VALUES ('Dasha', 'd@sh@.ru')""")

conn.commit()# сохраняем
# дополняем значения в таблицу автомобиля
c.execute("""INSERT INTO cars (model, user_id) VALUES ('Mersedes', 1)""")
c.execute("""INSERT INTO cars (model, user_id) VALUES ('BMW', 2)""")
c.execute("""INSERT INTO cars (model, user_id) VALUES ('Lada', 3)""")
c.execute("""INSERT INTO cars (model, user_id) VALUES ('KIA', 4)""")
c.execute("""INSERT INTO cars (model, user_id) VALUES ('Opel', 5)""")

c.execute("""SELECT users.id, users.name, users.email, \
            model FROM users LEFT JOIN cars c ON users.id=user_id""")# склейка двух таблиц

conn.commit()# сохраняем

print('id\t', 'name\t', 'email\t', 'car\t')# отображение столбцов в консоле

for row in c.fetchall():# выведет все значения добавленные изначально в таблицуу
    print(*row, sep='\t')


enter = input('Введите id:')

c.execute(f"SELECT name FROM users WHERE id = (?)", (enter))# проверка по id номеру
for i in c.fetchall():
    print(i[0])

name = input('введите имя: ')

email = input('введите email: ')

c.execute(f"SELECT name FROM users WHERE name = '{name}'") # проверяем и добовляем значения в таблицу
if c.fetchone() is None:
    c.execute(f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')")
    conn.commit()
    for row in c.fetchall():
        print(*row, sep='\t')
        print('успешно зарегистрирован')
else:
    print('данная форма уже присутсвует!')
for row in c.execute("""SELECT * FROM users"""):
    print(*row, sep='\t')

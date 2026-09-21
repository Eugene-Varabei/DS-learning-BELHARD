import sqlite3
# создание подключения к БД
con=sqlite3.connect('myDatabase.db')
# создаем "курсор" (спец объект для взаимодействия с содержимым БД)
cursor=con.cursor()

# строка содержит sql запрос на созжание табл
# sql= 'CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, name Text, age INTEGER);'
# # выполнение скл запроса на создание таблицы в БД
# cursor.execute(sql)

# добавление данных в БД
# name='Петров'
# age=35
# name=input('Write name: ')
# age=int(input('write age: '))
# sql=f'INSERT INTO users(name, age) VALUES ("{name}",{age});'
# cursor.execute(sql)
# # подтверждение транзакции в случ запроса на изменение содержимого БД
# con.commit()

# #безопасное добавление данных в БД
# name=input('Write name: ')
# age=int(input('Write age: '))
# # кортеж для хранения данныхъ для БД
# data=(name, age)
# sql='INSERT INTO users(name, age) VALUES (?, ?);'
# cursor.execute(sql, data)
# con.commit()

# выполнение множ запроса на запись в БД
# чтение данных из файлы в список кортежей
# usersList=[]
# with open('test.txt','r') as file:
#     while True:
#         line=file.readline()
#         if line == '':
#             break
#         if line[-1]=='\n':
#             line=line[:-1]
#         usersList.append(tuple(line.split(';; ')))
#
# # произведем запись в бд множество данных
# sql='INSERT INTO users(name, age) VALUES (?, ?);'
# cursor.executemany(sql, usersList)
# con.commit()

# чтение всех данных из таблицы БД
# sql='SELECT * FROM users'
# cursor.execute(sql)
# # перебор содержимого курсора (всех данных из курсора)
# for user in cursor.fetchall():
#     print(user)
    # print(f'ID: {user[0]}, name: {user[1]}, age: {user[2]}.')
# sql='SELECT name,age FROM users WHERE age BETWEEN 30 and 50'
# cursor.execute(sql)
# # перебор содержимого курсора (всех данных из курсора)
# for user in cursor.fetchall():
#     print(user)

# агрегатные функции
# ср арифм AVG(), MIN() MAX(), SUM(), COUNT(без параметров)
# sql='SELECT COUNT() FROM users WHERE age BETWEEN 30 and 50'
# cursor.execute(sql)
# res=cursor.fetchone()
# print(*res)

# обновдяение данных
# sql = 'UPDATE users SET age=25 WHERE name="Иванов"'
# cursor.execute(sql)
# con.commit()

# удаление данных
# sql='DELETE FROM users WHERE id = 7;'
# cursor.execute(sql)
# con.commit()

#закрытие подкл к БД
cursor.close()
con.close()

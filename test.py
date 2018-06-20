import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# create_table = "CREATE TABLE users (ID int, username text, password text)"
#
# cursor.execute(create_table)

# user = (1, 'lynne', 'abc')
# insert_query = "INSERT INTO users VALUES (?,?,?)"
# cursor.execute(insert_query, user)
# connection.commit()

# users = [
#     (2, 'reda', 'abc'),
#     (3, 'nancy', 'abc'),
#     (4, 'johanne', 'abc')
# ]
# insert_query = "INSERT INTO users VALUES (?,?,?)"
# cursor.executemany(insert_query, users)
# connection.commit()

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)



cursor.close()
connection.close()

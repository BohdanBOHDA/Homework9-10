import sqlite3

connection = sqlite3.connect("AnimalKingdom.sl3", 5)
cur = connection.cursor()

cur.execute("SELECT rowid, name, type FROM animals;")
connection.commit()
# Спочатку я написав UPDATE animals SET name='Сокіл' WHERE rowid=3;
#              потім SELECT name FROM animals WHERE type='Ссавець';
#                    SELECT rowid, name, type FROM animals;

result = cur.fetchall()
print(result)
print(connection)
print(cur)
connection.close()

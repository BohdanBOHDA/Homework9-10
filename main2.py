import sqlite3

connection = sqlite3.connect("AnimalKingdom.sl3", 5)
cur = connection.cursor()

cur.execute("INSERT INTO animals (name, type) VALUES ('Мавпа', 'Ссавець');")
connection.commit()

# спочатку я написав у лапках "CREATE TABLE animals (name TEXT, type TEXT);"
# потім INSERT INTO animals (name, type) VALUES ('Лев', 'Ссавець');
#       INSERT INTO animals (name, type) VALUES ('Крокодил', 'Плазун');
#       INSERT INTO animals (name, type) VALUES ('Орел', 'Птах');
#       INSERT INTO animals (name, type) VALUES ('Морська черепаха', 'Плазун');
#       INSERT INTO animals (name, type) VALUES ('Мавпа', 'Ссавець');

print(connection)
print(cur)
connection.close()

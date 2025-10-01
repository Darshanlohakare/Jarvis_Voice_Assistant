import csv
import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name varchar(100), path varchar(1000))"
cursor.execute(query)

#query = "INSERT INTO sys_command VALUES(NULL,'one note','C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013.exe')"
#cursor.execute(query)
#con.commit()

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name varchar(100), url varchar(1000))"
#cursor.execute(query)

#query = "INSERT INTO web_command VALUES(NULL,'youtube','https://www.youtube.com/')"
#cursor.execute(query)
#con.commit()


#app_name = "one note"
#cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
#results = cursor.fetchall()
#print(results[0][0])

# Create a table with the desired columns
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# # Specify the column indices you want to import (0-based index)
# # Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 21]

# # # Read data from CSV and insert into SQLite table for the desired columns
# import csv

# # Connect to your database
# conn = sqlite3.connect("contacts.db")
# cursor = conn.cursor()


# with open('contacts.csv', newline='', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     header = next(reader)  # Skip header row
#     rows = list(reader)

# # Update these indices to match your desired columns
# desired_columns_indices = [0, 21]  # For example: 0 = First Name, 21 = Phone 1 - Value

# for row in rows:
#     if all(i < len(row) for i in desired_columns_indices):
#         selected_data = [row[i] for i in desired_columns_indices]
#         name = selected_data[0]
#         mobile_no = selected_data[1]
#         cursor.execute('''INSERT INTO contacts (id, name, mobile_no) VALUES (null, ?, ?);''', (name, mobile_no))
#     else:
#         print(f"Skipping incomplete row: {row}")

# conn.commit()
# conn.close()

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 20]

# # # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# con.commit()
# con.close()

# query = "INSERT INTO contacts VALUES (null,'Darshan', '1234567890', 'null')"
# cursor.execute(query)
# con.commit()

# query = 'darshan'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])
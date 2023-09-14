import sqlite3

# Define the list of file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'Data.pdf', 'myPhoto.jpg')

# Creates a SQLite database
conn = sqlite3.connect('file_database.db')
cursor = conn.cursor()

# Create a table in the database
cursor.execute('''CREATE TABLE IF NOT EXISTS files (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filename TEXT
                )''')

# for loop that iterates through the list of file 
# names and inserts .txt files as database entries
for filename in fileList:
    if filename.endswith('.txt'):
        cursor.execute("INSERT OR REPLACE INTO files (filename) VALUES (?)", (filename,))

# Commit the changes to the database
conn.commit()

# Query the database and print the qualifying text files
print("Qualifying text files:")
cursor.execute("SELECT filename FROM files WHERE filename LIKE '%.txt'")
qualifying_files = cursor.fetchall()
for file in qualifying_files:
    print(file[0])

# Close the database connection
# to prevent memory leaks (as explained 
# in one of the previous videos)
conn.close()
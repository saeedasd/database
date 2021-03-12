import sqlite3

conn = sqlite3.connect('project.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Instrument(
instrument_id INTEGER NOT NULL PRIMARY KEY,
instrument_image BLOB,
instrument_name Varchar(45)
 )""")


c.execute("""CREATE TABLE IF NOT EXISTS Projects (
project_id INTEGER PRIMARY KEY,
description TEXT NOT NULL
)""")

c.execute("""CREATE TABLE IF NOT EXISTS Project_list(project_id INTEGER NOT NULL REFERENCES Projects(project_id),
instrument_id INTEGER NOT NULL REFERENCES Instruments(instrument_id),
PRIMARY KEY(project_id))""")

c.execute("""CREATE TABLE IF NOT EXISTS users_projects_list (
create_time DATETIME,
user_id INTEGER,
project_id INTEGER,
PRIMARY KEY(user_id, project_id)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS userToken(
token_id INTEGER PRIMARY KEY,
create_time DATETIME)""")

c.execute("""CREATE TABLE IF NOT EXISTS Users(
user_id INTEGER PRIMARY KEY,
username VARCHAR(16),
create_time DATETIME,
user_type BINARY,
age INTEGER,
email VARCHAR(40),
password VARCHAR(32),
user_token VARCHAR(45),
FOREIGN KEY(user_token) REFERENCES userToken (token_id)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS Sounds (
sound_id INTEGER NOT NULL PRIMARY KEY,
sound_name VARCHAR(45),
instrument_id INTEGER,
recording VARCHAR(45),
FOREIGN KEY(instrument_id) REFERENCES Instruments (instrument_id)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS Device(
session_id INTEGER PRIMARY KEY,
dev INTEGER,
release_ver FLOAT)""")

#c.execute("INSERT INTO Sounds VALUES (2, 'electric guitar', 3, 'sounds/electric_guitar.wav')")

c.execute("SELECT * from Sounds")

print(c.fetchall())
conn.commit()
conn.close()

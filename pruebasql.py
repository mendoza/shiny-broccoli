import pyodbc

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = "localhost"
database = "TestDB"
username = "SA"
password = "Rockero99"
cnxn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
    + server
    + ";DATABASE="
    + database
    + ";UID="
    + username
    + ";PWD="
    + password
)
cursor = cnxn.cursor()

# Sample select query
cursor.execute("SELECT * from inventory;")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()

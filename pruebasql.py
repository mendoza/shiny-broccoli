import pyodbc

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = "localhost,1433"
database = "PRUEBA"
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
print(cnxn)
"""# Sample select query
cursor.execute("SELECT * from inventory;")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()"""

import mysql.connector
import mysql

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Macmac93SQL",
    database = "pysport"
)

my_cursor = mydb.cursor()

my_cursor.execute("SHOW DATABASES")


for db in my_cursor:
    print (db)

my_cursor = mydb.cursor()

my_cursor.execute("SHOW TABLES")

for table in my_cursor:
    print (table)


# mycursor = db.cursor()
# mycursor.execute("CREATE SCHEMAS newdb")
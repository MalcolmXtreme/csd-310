import mysql.connector
import mysql

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Macmac93SQL",
    database = "pysport"
)

my_cursor = mydb.cursor()

delete_query = "DELETE FROM player2"

my_cursor.execute(delete_query)



mydb.commit()
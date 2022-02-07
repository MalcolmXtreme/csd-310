import mysql.connector
import mysql

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Macmac93SQL",
    database = "pysport"
)



my_cursor = mydb.cursor()

my_cursor.execute("SELECT team_id, team_name, mascot FROM teams")

teams = my_cursor.fetchall()

for team in teams:
    print("Team Name:{}”.format(team[1])")

# SELECT team_id, team_name, mascot FROM team

# MySQL: Select Query 
# SELECT <column_name>, <column_name> FROM <table_name>;
# Example
# SELECT team_id, team_name, mascot FROM team;

# Cursor Example
# cursor = db.cursor()

# cursor.execute(“SELECT team_id, team_name, mascot FROM team”)

# teams = cursor.fetchall()

# for team in teams:
# print(“Team Name: {}”.format(team[1]))



# for db in my_cursor:
#     print (db)

# my_cursor = mydb.cursor()

# my_cursor.execute("SHOW TABLES")

# for table in my_cursor:
#     print (table)


# mycursor = db.cursor()
# mycursor.execute("CREATE SCHEMAS newdb")
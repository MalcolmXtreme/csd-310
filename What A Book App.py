from unittest.util import three_way_cmp
import mysql.connector
import mysql

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Macmac93SQL",
    database = "whatabook_user"
  
)

mycursor= mydb.cursor()


def welcome():
      print("Hello, Welcome to What A Book! ")

      input("Press Enter to continue...") 

      return mainmenu()

# This is the Mainmenu function, initially branching from the welcome screen, it includes three
# main options leading to the database books list, location list, and the user home.
 
def mainmenu():

     # mycursor= mydb.cursor()
    
     select = int (input("\nMain Menu:\n Options -\n 1) View Books\n 2) View Location\n 3) My Account \n "))
      
     if select == 1:
                 return view_books()
      
     if select == 2:
                 return view_locale()
      
     if select == 3:
                 return view_user()


def view_books():
       print("\n Here is our selections:\n")
       mycursor.execute("SELECT * FROM books")

       myresult = mycursor.fetchall()

       for row in myresult: 
            print(row)
      
       input ("Hit Enter For Main Menu...")
       return mainmenu()


def view_locale():
       print("\n Here is our locations:\n")
       mycursor.execute("SELECT * FROM store")

       myresult = mycursor.fetchall()

       for row in myresult: 
            print(row)
      
       input ("Hit Enter For Main Menu...")
       return mainmenu()


def view_user():
     
     print(" \nWhat A Book User Home \n_____________________\n ")

     user_entry = int (input("What is your What A Book I.D number?\n "))

     if user_entry == 1: 
          
           return view_user1()
     
      
     if user_entry == 2: 
          
           return view_user2()
     
        
     if user_entry == 3: 
          
           return view_user3()
          

# The functions below are meant to pull from the users table, for each user I made a function.
# There might be a more effiecient way in pulling from the database without defining each user 
# for referencing, however for me this worked. 


# Note the for loops within the view_user functions technically work. Incase current method fails in developement 
# for any reason will return to for loop. 


def view_user1():
     
     print("\nWelcome Back! ")  

     mycursor.execute("SELECT * FROM users")


     record1 = mycursor.fetchone()
     
     record2 = mycursor.fetchone()

     record3 = mycursor.fetchone()

     print(record1)

     user_select = int (input("\nOptions -\n 1) Main Menu\n 2) My Wishlist\n "))

     if user_select == 1:
               return mainmenu()
     
     elif user_select == 2:
               return view_wishlist()

     # for row in record1:
     #      print(row)

def view_user2():

     print("\nWelcome Back! ")  

     mycursor.execute("SELECT * FROM users")

     record1 = mycursor.fetchone()
     
     record2 = mycursor.fetchone()

     record3 = mycursor.fetchone()

     print(record2)

     user_select = int (input("\nOptions -\n 1) Main Menu\n 2) My Wishlist\n "))

     if user_select == 1:
               return mainmenu()

     elif user_select == 2:
               return view_wishlist()

     

     # for row2 in record2:
     #      print(row2)

def view_user3():
      
      print("\nWelcome Back! ")  

      mycursor.execute("SELECT * FROM users")

      record1 = mycursor.fetchone()
     
      record2 = mycursor.fetchone()

      record3 = mycursor.fetchone()

      print(record3)

      user_select = int (input("\nOptions -\n 1) Main Menu\n 2) My Wishlist\n "))

      if user_select == 1:
               return mainmenu()
      elif user_select == 2:
               return view_wishlist()



def view_wishlist():

    
     mycursor.execute("SELECT * FROM books INNER JOIN wishlist")

     myresult2 = mycursor.fetchall()

     for row in myresult2: 
            print(row)



     # mycursor.execute("SELECT * FROM wishlist WHERE book_id = 9,7,2")

    

     







     

welcome()




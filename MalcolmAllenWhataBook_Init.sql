#   Name: Malcolm Allen 
#   Class: Data Security
#   3/5/22
    #create user
#Malcolm Allen What A Book App.py

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MacMacSQL93'

/*#create tables*/
CREATE TABLE store (
    store_id INT    NOT NULL   AUTO_INCREMENT,
    name VARCHAR(50)  NOT NULL,
    locale VARCHAR(500) NOT NULL,
    
    PRIMARY KEY(ID)
);
CREATE TABLE book(
    book_id INT     NOT NULL    AUTO_INCREMENT,
    book_name VARCHAR(100)  NOT NULL, 
    author VARCHAR(200) NOT NULL,
    PRIMARY KEY(book_id)
);
CREATE TABLE user(
    user_id INT     NOT NULL    AUTO_INCREMENT,
    first_name VARCHAR(100)  NOT NULL,
    last_name VARCHAR(200)  NOT NULL,
    PRIMARY KEY(user_id)
);
CREATE TABLE wishlist(
    wishlist_id INT  NOT NULL AUTO_INCREMENT,
    user_id INT  NOT NULL,
    book_id INT  NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
	REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY(user_id)
	REFERENCES user(user_id)


);
/*#insert location*/
INSERT INTO store(name,locale)
   VALUES ( 'What A Book ', 'Barnesoble BLVD, Kissimee, FL, 34746');
INSERT INTO store(name,locale)
   VALUES ( 'What A Book', 'Yosville RD, Ashton, NY 55312');
INSERT INTO store(name,locale)
   VALUES ( 'What A Book ', 'Little RD. Dallas, TX, 75043');

/*#insert books*/
INSERT INTO book(book_name, author)
    VALUES('Harry Potter', 'J.K Rowling');
INSERT INTO book(book_name, author)
    VALUES( '12 Rules for Life', 'Jordan Peterson');
INSERT INTO book(book_name, author)
    VALUES('Gregor the Overlander', 'Suzanne Collins');
INSERT INTO book(book_name, author)
    VALUES('The Right Side Of History',  'Ben Shapiro');
INSERT INTO book(book_name, author)
    VALUES('The Notebook', 'Nicholas Sparks');
INSERT INTO book(book_name, author)
    VALUES('The Hunger Games', 'Suzanne Collins');
INSERT INTO book(book_name, author)
    VALUES('Pride and Prejudice and Zombies', 'Seth Grahame-Smith');
INSERT INTO book(book_name, author)
    VALUES('City of Bones', 'Cassandra Clare');
INSERT INTO book(book_name, author)
    VALUES( 'City of Ashes', 'Cassandra Clare');

/*#insert users*/
INSERT INTO user(first_name, last_name)
    VALUES('Jackson', 'Skill');
INSERT INTO user(first_name, last_name)
    VALUES('Tera', 'Lightly');
INSERT INTO user(first_name, last_name)
    VALUES('Nolan', 'Kristoff');

SELECT `users`.`user_id`,
    `users`.`first_name`,
    `users`.`last_name`
FROM `whatabook_user`.`users`;

SELECT `books`.`book_id`,
    `books`.`book_name`,
    `books`.`author_name`
FROM `whatabook_user`.`books`;

SELECT `users`.`user_id`,
    `users`.`first_name`,
    `users`.`last_name`
FROM `whatabook_user`.`users`;

SELECT `wishlist`.`wishlist_id`,
    `wishlist`.`user_id`,
    `wishlist`.`book_id`
FROM `whatabook_user`.`wishlist`;
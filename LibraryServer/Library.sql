CREATE TABLE ADMINS(
	Username varchar(20),
	Password varchar(20),
	PRIMARY KEY(Username)
);

CREATE TABLE USERS(
	Username varchar(20),
	Password varchar(20),
	PRIMARY KEY(Username)
);

CREATE TABLE BOOKS(
	Book_ID char(5),
	Book_name varchar(100),
	Author varchar(70),
	Book_type varchar(30),
	Book_format char(5),
	Book_link varchar(50),
	PRIMARY KEY(Book_ID)
);

insert into ADMINS values('root1', '19120106');
insert into ADMINS values('root2', '19120256');

insert into USERS values('knvtt','123');

insert into BOOKS values('T0001','Computer networking a top-down approach', 'James F. Kurose, Keith W. Ross', 'Technology', 'txt', 'Database\Computer networking a top-down approach.txt');
insert into BOOKS values('T0002', 'CLean code', 'Robert Martin', 'Technology', 'txt', 'Database\Clean code.txt');
insert into BOOKS values('CS001','Algorithms to Live By: The Computer Science of Human Decisions', 'Brian Christian', 'Computer Science', 'txt', 'Database\Algorithms to Live By.txt');
insert into BOOKS values('N0001','Tam quoc dien nghia', 'La Quan Trung', 'Novel', 'txt', 'Database\Tam quoc dien nghia.txt');
insert into BOOKS values('N0002','The Call of the Wild', 'Jack London', 'Novel', 'txt', 'Database\The Call of the Wild.txt');






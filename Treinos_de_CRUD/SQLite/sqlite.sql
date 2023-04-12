create table users(
	id int primary key,
	name varchar(50),
	login varchar(50),
	senha varchar(50)
);

SELECT * FROM users;

DROP TABLE users;

insert into users values (2, "maria", "maria@email", "12345678");
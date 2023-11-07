show databases;
create database test;
use test;

create table users (
  name varchar(255) primary key,
    password varchar(255) not null
);

insert into users values('Alua', 'alua');
insert into users values('Ali', 'ali');
insert into users values('Jandaulet', 'jandaulet');
insert into users values('Aisha', 'aisha');

select * from users;

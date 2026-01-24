-- create database
create database mrv_dsc;
-- to display list of databases
show databases;
-- select database
use mrv_dsc;
-- show current database
select database();
create table student(
id int,
name varchar(100),
course varchar(100),
fee int
);
-- to dislay tables
show tables;
-- insert single row into the table 
insert into student(id,name,course,fee)
values(186,'Avinash','csd_c',10000000);
select * from student;
-- secound row into the table
insert into student(id,name,course,fee)
values(233,'Rehan','csd_c',12400000);
select * from student;
-- third row into the table
insert into student(id,name,course,fee)
values(206,'Kevin','csd_c',200000);
select * from student;
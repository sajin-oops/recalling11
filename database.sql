mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sajin              |
| sajinak            |
| world              |
+--------------------+
6 rows in set (0.00 sec)

mysql> use sajinak;
Database changed
mysql> create table student(
    -> name varchar(30) notnull);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'notnull)' at line 2
mysql> name varchar(30) not null
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'name varchar(30) not null
)' at line 1
mysql> name varchar(30) not null,
    -> regno varchar(20) unique,
    -> email varchar(30) unique'
    '>
    '> ';
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'name varchar(30) not null,
regno varchar(20) unique,
email varchar(30) unique'

' at line 1
mysql> create table student(
    -> name varchar(30) not null,
    -> regno varchar(20) unique,
    -> email varchar(30) unique,
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ')' at line 5
mysql> create table student(
    -> name varchar(30) not null,
    -> regno varchar(20) unique,
    -> email varchar(30) unique,
    -> password varchar(30)not null
    -> );
Query OK, 0 rows affected (0.07 sec)

mysql> desc student;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| name     | varchar(30) | NO   |     | NULL    |       |
| regno    | varchar(20) | YES  | UNI | NULL    |       |
| email    | varchar(30) | YES  | UNI | NULL    |       |
| password | varchar(30) | NO   |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
4 rows in set (0.01 sec)

mysql> select * from student;
Empty set (0.01 sec)

mysql> insert into student values(""S\
    -> \\\\s;
ERROR:
Unknown command '\\'.
ERROR:
Unknown command '\\'.
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'S
\\\\s' at line 1
mysql> insert into student values("sajin a.k",111,"sajinak2003@gmail.com",1223);
Query OK, 1 row affected (0.01 sec)

mysql> select*from student;
+-----------+-------+-----------------------+----------+
| name      | regno | email                 | password |
+-----------+-------+-----------------------+----------+
| sajin a.k | 111   | sajinak2003@gmail.com | 1223     |
+-----------+-------+-----------------------+----------+
1 row in set (0.00 sec)

mysql> update student set password = 12345 where regno=111;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select*from student;
+-----------+-------+-----------------------+----------+
| name      | regno | email                 | password |
+-----------+-------+-----------------------+----------+
| sajin a.k | 111   | sajinak2003@gmail.com | 12345    |
+-----------+-------+-----------------------+----------+
1 row in set (0.00 sec)

mysql> insert into student values("nijas a.k",222,"nijas2@gmail.com",23122);
Query OK, 1 row affected (0.00 sec)

mysql> select * from student;
+-----------+-------+-----------------------+----------+
| name      | regno | email                 | password |
+-----------+-------+-----------------------+----------+
| sajin a.k | 111   | sajinak2003@gmail.com | 12345    |
| nijas a.k | 222   | nijas2@gmail.com      | 23122    |
+-----------+-------+-----------------------+----------+
2 rows in set (0.00 sec)

mysql> delete student where rego = 222;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'where rego = 222' at line 1
mysql> delete student where regno = 222;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'where regno = 222' at line 1
mysql> delete from student where regno = 222;
Query OK, 1 row affected (0.00 sec)

mysql> select * from student;
+-----------+-------+-----------------------+----------+
| name      | regno | email                 | password |
+-----------+-------+-----------------------+----------+
| sajin a.k | 111   | sajinak2003@gmail.com | 12345    |
+-----------+-------+-----------------------+----------+
1 row in set (0.00 sec)
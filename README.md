# Darasa (Islamic) School Management System
**Backend Microservice Python** :wave:

## Description
Berisikan implementasi aplikasi _**Backend**_ pada **school system database management** dan juga _**microservice**_ dalam bentuk REST API.

**DB** :
* SQL  -> all table (kecuali educational table)
* NoSQL -> only educational table (di mongodbapp)
 
![1](https://user-images.githubusercontent.com/23287190/124367013-1ae2e700-dc7e-11eb-8197-02235191691f.png)

**Framework** :
* Flask  
* FastAPI 
* JWT

**ERD** :

![erd](https://user-images.githubusercontent.com/23287190/124358916-b78c9100-dc4c-11eb-8769-648a45f90435.png)

## Persiapan database
untuk database berikut script initial yang digunakan :
pembuatan **database**
```
@membuat database:
CREATE DATABASE school;
USE school;
```

pembuatan **tabel**
```
@membuat table parent:
create table parent (
    parent_id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    username varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    nama varchar(255) NOT NULL,
    phone varchar(255) NULL
);

@membuat table teacher:
create table teacher (
    teacher_id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    username varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    nama varchar(255) NOT NULL,
    phone varchar(255) NULL,
    is_guardian_teacher BOOLEAN NOT NULL
);

@membuat table class:
create table class (
    class_id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    namakelas varchar(255) NOT NULL,
    educational_id INT NULL,
    teacher_id INT NULL,
    seats INT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id)
);

@membuat table student:
create table student (
    siswa_id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    username varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    namadepan varchar(255) NOT NULL,
    namabelakang varchar(255) NOT NULL,
    parent_id int NULL,
    class_id int NULL,
    FOREIGN KEY (parent_id) REFERENCES parent(parent_id),
    FOREIGN KEY (class_id) REFERENCES class(class_id)
);

@membuat table subject:
create table subject (
    subject_id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    matapelajaran varchar(255) NOT NULL,
    kode varchar(255) NULL,
    class_id INT NULL,
    FOREIGN KEY (class_id) REFERENCES class(class_id)
);

@membuat table jadwal:
create table jadwal (
    jadwal_id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    hari varchar(255) NULL,
    class_id INT NULL,
    FOREIGN KEY (class_id) REFERENCES class(class_id)
);

@membuat table sesi:
create table sesi (
    sesi_id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    jadwal_id INT NOT NULL,
    subject_id INT NULL,
    time_start time(0) NULL,
    time_end time(0) NULL,
    teacher_id INT NULL,
    FOREIGN KEY (jadwal_id) REFERENCES jadwal(jadwal_id),
    FOREIGN KEY (subject_id) REFERENCES subject(subject_id),
    FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id)
);

```

contoh pengisian **column/field** via sql
```
-- insert data parent
insert into parent 
	(username,email,nama,phone)
values
	('ridwan','ridwan@gmail.com','ridwan','1212312');
    
-- insert data teacher
insert into teacher
	(username,email,nama,phone,is_guardian_teacher)
values
	('marwan','marwan@gmail.com','marwan','1212314212','0');
    
-- insert class
insert into class
	(namakelas,educational_id,teacher_id,seats)
values
	('3','1',3,5);

-- insert subject
insert into subject
	(matapelajaran, kode,class_id)
values
	('matematika','sb001',1);
    
-- insert jadwal
insert into jadwal
	(hari,class_id)
values
	('senin',1);
    
-- insert sesi
insert into sesi
	(jadwal_id,subject_id, time_start,time_end, teacher_id)
values
	(1,1,'07:00','08:30',1);
    
-- insert student
insert into student
	(username,email,namadepan,namabelakang,parent_id,class_id)
values
	('riski','riski@gmail.com','riski','rohim',1,1);
```

## Installation Libraries
Using python 3.x series 
```
pip install flask
pip install fastapi
pip install uvicorn
pip install mysql-connector-python
pip install pymongo
pip install mongoengine
pip install sqlalchemy
pip install flask-jwt-extended
```

## REST API
REST APIs documentation (using **postman**) is described below.

> **for better REST APIs documentation view** : https://documenter.getpostman.com/view/14230433/Tzm2Jxv2#9fdeb1c7-747d-4b98-948c-0d34744c40f7

### Get List of things

#### Request
'GET ....'

#### Response
'''
......
'''

### Create a new thing

#### Request
'POST ....'

#### Response
'''
......
'''

### Change a thing

#### Request
'PUT ....'

#### Response
'''
......
'''

### Delete a Thing 

#### Request
'DELETE ....'

#### Response
'''
......
'''

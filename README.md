# Darasa (Islamic) School Management System
Tugas Akhir SanberCode : **Backend Microservice Python Batch 25** :wave:

## Description
Berisikan implementasi aplikasi _**Backend**_ pada **school system database management** dan juga _**microservice**_ dalam bentuk REST API.

**DB** :
* SQL  -> all table (kecuali educational table)
* NoSQL -> only educational table (di mongodbapp)
 
![1](https://user-images.githubusercontent.com/23287190/124367013-1ae2e700-dc7e-11eb-8197-02235191691f.png)

**Features** :
* ORM / ODM


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

### 1. Parent Table

#### Get parents
`GET localhost:5000/parents`

> Response
```
[
    {
        "id": 1,
        "username": "ridwan",
        "email": "ridwan@gmail.com",
        "nama": "ridwan",
        "phone": "1212312"
    },
    {
        "id": 2,
        "username": "RK",
        "email": "faris@gmail.com",
        "nama": "faris",
        "phone": "0821312"
    },
    {
        "id": 4,
        "username": "zidan",
        "email": "farisy@gmail.com",
        "nama": "faris123",
        "phone": ""
    },
    {
        "id": 5,
        "username": "jamil",
        "email": "saifuljamil@gmail.com",
        "nama": "saifuludin",
        "phone": " 9812321312"
    }
]
```
#### Get parent
`GET localhost:5000/parent`

> BODY
```
{
    "parent_id" : 4
}
```
> Response
```
{
    "id": 4,
    "username": "zidan",
    "email": "farisy@gmail.com",
    "nama": "faris123",
    "phone": ""
}
```
#### Get parent token 
`GET localhost:5000/parent/request_token`

> BODY
```
{
    "email":"ridwan@gmail.com"
}
```
> Response
```
{
    "data": {
        "username": "ridwan",
        "email": "ridwan@gmail.com"
    },
    "token_access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjI1Mzc1NDA1LCJqdGkiOiIwN2VmYzkzNS1mM2IxLTRhMzctYTk1My1mOTY4NjllMjJmOTIiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7InVzZXJuYW1lIjoicmlkd2FuIiwiZW1haWwiOiJyaWR3YW5AZ21haWwuY29tIn0sIm5iZiI6MTYyNTM3NTQwNSwiZXhwIjoxNjI1NDYxODA1fQ.IPV5fd8K-DdXP7SIM3iXcg1IF_W3sS3CRiQlRmLLi5A"
}
```
#### Put parent
mengedit isi table parent
`PUT localhost:5000/parent`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "parent_id" : 5,
    "data": {
        "phone": " 9812321312",
        "email":"saifuljamil@gmail.com",
        "username":"jamil",
        "nama":"saifuludin"
    }
}
```
> Response
```
{
    "message": "Parent dengan Id 5 berhasil diupdate"
}
```
#### Delete parent
`DELETE localhost:5000/parent`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "parent_id" : 5
}
```
> Response
```
{
    "message": "Parent dengan Id 5 berhasil dihapus"
}
```

### 2. Teacher Table

#### Get teachers

`GET localhost:5000/teachers`

> Response
```
[
    {
        "id": 1,
        "username": "ridwan",
        "email": "ridwan@gmail.com",
        "nama": "ridwan",
        "phone": "1212312",
        "guardian_teacher": 1
    },
    {
        "id": 3,
        "username": "raffasya",
        "email": "raffasya@gmail.com",
        "nama": "raffa",
        "phone": "0812312412312",
        "guardian_teacher": 1
    }
]
```

#### Get teacher
get teacher by id

`GET localhost:5000/teacher`

> BODY
```
{
    "teacher_id" : 3
}
```
> Response
```
{
    "id": 3,
    "username": "raffasya",
    "email": "raffasya@gmail.com",
    "nama": "raffa",
    "phone": "0812312412312",
    "guardian_teacher": 1
}
```
#### Get teacher token
`GET localhost:5000/teacher/request_token`

> BODY
```
{
    "email": "marwan@gmail.com"
}
```
> Response (Succed)
```
{
    "data": {
        "username": "ridwan",
        "email": "ridwan@gmail.com"
    },
    "token_access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjI1Mzc2MDczLCJqdGkiOiIzYTQ5ZGJmMi0yMzAyLTQ4YmYtODdkMi02NzIwYWQ0MmMyZjEiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7InVzZXJuYW1lIjoicmlkd2FuIiwiZW1haWwiOiJyaWR3YW5AZ21haWwuY29tIn0sIm5iZiI6MTYyNTM3NjA3MywiZXhwIjoxNjI1NDYyNDczfQ.EZe4yfBGTbu9oK1YbA0jFyYEwXKxXgJj3rQhw-D0qgM"
}
```
> Response (Fail)
```
{
    "message": "Email tidak terdaftar"
}
```
#### Post teacher 
create teacher record

`POST localhost:5000/teacher`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "data" : {
        "username" :"raffasya",
        "email" : "raffasya@gmail.com",
        "phone":"2131251212312",
        "nama": "raffasya",
        "is_guardian_teacher": "1"
    }
}
```
> Response
```
{
    "message": "Teacher succesfully created",
    "code": "200"
}
```
#### Put teacher 
edit teacher by id

`PUT localhost:5000/teacher`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "teacher_id" :3,
    "data" : {
        "nama" :"raffa",
        "phone" :"0812312412312"
    }
}
```
> Response
```
{
    "message": "Teacher succesfully edited",
    "code": "201"
}
```
#### Delete teacher 
delete teacher by id

`DELETE localhost:5000/teacher`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "teacher_id" : 2
}
```
> Response
```
{
    "message": "Teacher succesfully deleted",
    "code": "201"
}
```
### 3. Student Table

#### Get Student 
get student by id

`GET localhost:5000/students`
> BODY
```
{
    "siswa_id":1
}
```

> Response
```
{
    "id": 1,
    "username": "riski",
    "email": "riski@gmail.com",
    "namadepan": "riski",
    "namabelakang": "rohim",
    "parent_id": 1,
    "class_id": 1
}
```
#### Get students

`GET localhost:5000/students`

> Response
```
[
    {
        "id": 1,
        "username": "riski",
        "email": "riski@gmail.com",
        "namadepan": "riski",
        "namabelakang": "rohim",
        "parent": 1,
        "class_id": 1
    },
    {
        "id": 3,
        "username": "mikio",
        "email": "mikio@gmail.com",
        "namadepan": "miko",
        "namabelakang": "kaoru",
        "parent": 1,
        "class_id": 1
    }
]
```
#### GET student token
`GET localhost:5000/student/request_token`

> BODY
```
{
    "email": "riski@gmail.com"
}
```
> Response
```
{
    "data": {
        "username": "riski",
        "email": "riski@gmail.com"
    },
    "token_access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjI1Mzc2NTk0LCJqdGkiOiJjYzI3NTExMS1mYTYwLTQ0NzItYTk0OS04MWM0MjBhZjYwNmQiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7InVzZXJuYW1lIjoicmlza2kiLCJlbWFpbCI6InJpc2tpQGdtYWlsLmNvbSJ9LCJuYmYiOjE2MjUzNzY1OTQsImV4cCI6MTYyNTQ2Mjk5NH0.XGTqYahoqUdMyccb-PpdBhA0n-zxr2qvPRBGlrGh5tg"
}
```

#### Post student 
`POST localhost:5000/student`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{ "data" : 
        {
            "username" : "mikio",
            "email" : "mikio@gmail.com",
            "namadepan" : "miko",
            "namabelakang" : "kudo",
            "parent_id": "1",
            "class_id" : "1"
        }
}
```
> Response
```
{
    "message": "Student succesfully created",
    "code": "200"
}
```

#### Put student 
`PUT localhost:5000/student`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "siswa_id" :3,
    "data": {
        "namabelakang" : "kaoru"
    }
}
```
> Response
```
{
    "message": "Student succesfully edited",
    "code": "200"
}
```

#### Delete student 
`DELETE localhost:5000/student`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "siswa_id" : 2
}
```
> Response
```
{
    "message": "Siswa dengan Id 2 berhasil dihapus"
}
```

### 4. Subject Table

#### Get subjects
`GET localhost:5000/subjects`

> Response
```
[
    {
        "id": 1,
        "matapelajaran": "matematika",
        "kode_pelajaran": "sb001",
        "class_id": 1
    },
    {
        "id": 3,
        "matapelajaran": "kimia",
        "kode_pelajaran": "b003",
        "class_id": 1
    },
    {
        "id": 4,
        "matapelajaran": "kalkulus",
        "kode_pelajaran": "k003",
        "class_id": 1
    }
]
```
#### Get subject
`GET localhost:5000/subject`

> BODY
```
{
    "subject_id":1
}
```
> Response
```
{
    "id": 1,
    "matapelajaran": "matematika",
    "kode_pelajaran": "sb001",
    "class_id": 1
}
```
#### Delete subject
`DELETE localhost:5000/subject`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "subject_id": 2
}
```
> Response
```
{
    "message": "subject dengan Id 2 berhasil dihapus"
}
```

#### Put subject
`PUT localhost:5000/subject`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "subject_id" : 3,
    "data" : {
        "kode" : "b003"
    }
}
```
> Response
```
{
    "message": "Subject dengan Id 3 berhasil diupdate"
}
```

#### Post subject
`POST localhost:5000/subject`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{ "data" : {
            "matapelajaran" : "kalkulus",
            "kode" : "k003",
            "class_id": "1"
        }
}
```
> Response
```
{
    "message": "Subject succesfully created",
    "code": "200"
}
```
### 5. Class Table

#### Get class
`GET localhost:5000/class`

> Response
```
[
    {
        "class_id": 1,
        "namakelas": "3",
        "educational_id": 1,
        "teacher_id": 3,
        "seats": 5
    },
    {
        "class_id": 3,
        "namakelas": "4",
        "educational_id": 1,
        "teacher_id": 3,
        "seats": 30
    },
    {
        "class_id": 4,
        "namakelas": "2",
        "educational_id": 1,
        "teacher_id": 1,
        "seats": 44
    }
]
```
#### Get student class
`GET localhost:5000/class/students`

> BODY
```
{
    "class_id" : 1
}
```

> Response
```
[
    {
        "siswa_id": 1,
        "namadepan": "riski",
        "namabelakang": "rohim",
        "parent_id": 1,
        "class_id": 1
    },
    {
        "siswa_id": 3,
        "namadepan": "miko",
        "namabelakang": "kaoru",
        "parent_id": 1,
        "class_id": 1
    },
    {
        "siswa_id": 4,
        "namadepan": "miko",
        "namabelakang": "kudo",
        "parent_id": 1,
        "class_id": 1
    }
]
```
#### Delete class
`DELETE localhost:5000/class`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "class_id" : 2
}
```
> Response
```
{
    "message": "Class succesfully deleted",
    "code": "201"
}
```
#### Put class
`PUT localhost:5000/class`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "class_id" : 3,
    "data": {
        "seats":30
    }
}
```
> Response
```
{
    "message": "Class succesfully edited",
    "code": "201"
}
```
#### Post class
`POST localhost:5000/class`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "data": {
        "namakelas" :"2",
        "educational_id" : "1",
        "teacher_id":"1",
        "seats": "44"
    }
}
```
> Response
```
{
    "message": "Class succesfully created",
    "code": "200"
}
```

### 6. Jadwal Table

#### Get jadwal
`GET localhost:5000/jadwal`

> Response
```
[
    {
        "jadwal_id": 1,
        "hari": "kamis",
        "class_id": 1
    },
    {
        "jadwal_id": 2,
        "hari": "jumat",
        "class_id": 1
    }
]
```

#### Put jadwal
`PUT localhost:5000/jadwal`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "jadwal_id" : 1,
    "data" : {
        "hari" : "kamis"
    }
}
```
> Response
```
{
    "message": "Class succesfully edited",
    "code": "201"
}
```
#### Post jadwal
`POST localhost:5000/jadwal`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "data" : {
        "hari" : "jumat",
        "class_id" : 1
    }
}
```
> Response
```
{
    "message": "Class succesfully created",
    "code": "200"
}
```
#### Get sesi jadwal
`GET localhost:5000/jadwal/sesi`

> BODY
```
{
    "jadwal_id" : 1
}
```
> Response
```
[
    {
        "sesi_id": 1,
        "subject_id": 1,
        "time_start": "07:00:00",
        "time_end": "08:45:00",
        "teacher_id": 1
    },
    {
        "sesi_id": 3,
        "subject_id": 1,
        "time_start": "09:22:00",
        "time_end": "09:22:00",
        "teacher_id": 1
    }
]
```
### 7. Sesi Table

#### Get sesi
`GET localhost:5000/sesi`

> Response
```
[
    {
        "jadwal_id": 1,
        "subject_id": 1,
        "time_start": "07:00:00",
        "time_end": "08:45:00",
        "teacher_id": 1
    },
    {
        "jadwal_id": 1,
        "subject_id": 1,
        "time_start": "09:22:00",
        "time_end": "09:22:00",
        "teacher_id": 1
    }
]
```

#### Delete sesi
`DELETE localhost:5000/sesi`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "sesi_id" : 2
}
```
> Response
```
{
    "message": "Sesi succesfully deleted",
    "code": "201"
}
```
#### Put sesi
`PUT localhost:5000/sesi`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "sesi_id" : 1,
    "data" : {
        "time_end" : "08:45"
    }
}
```
> Response
```
{
    "message": "Sesi succesfully edited",
    "code": "201"
}
```
#### Post sesi
`POST localhost:5000/sesi`

> Authorization: Bearer Token
```
Token    <token>
```
> BODY
```
{
    "data" : {
        "subject_id" : "1",
        "jadwal_id" : "1",
        "time_start" : "09:22",
        "time_end" : "09:22",
        "teacher_id" : "1"
    }
}
```
> Response
```
{
    "message": "Sesi succesfully created",
    "code": "200"
}
```
### 7. Educational Table (FastAPI / Mongodb)

#### Get all educational
`GET localhost:8000/educationals`

> Response
```
[
    {
        "_id": "60e0c5496d70aed082bc112d",
        "educational_id": "2",
        "tingkat": "SD",
        "tahunajaran": "2021"
    },
    {
        "_id": "60e0c5546d70aed082bc112e",
        "educational_id": "3",
        "tingkat": "smp",
        "tahunajaran": 2021.0
    },
    {
        "_id": "60e0d246ea0ae6cfe0081ea3",
        "educational_id": "4",
        "tahunajaran": "2021",
        "tingkat": "SMA"
    }
]
```
#### Get educational
`GET localhost:8000/educational`

> BODY
```
{
    "id" : "60e0c5496d70aed082bc112d"
}
```
> Response
```
{
    "_id": "60e0c5496d70aed082bc112d",
    "educational_id": "2",
    "tingkat": "SD",
    "tahunajaran": "2021"
}
```

#### Delete educational
`DELETE localhost:8000/educational`

> BODY
```
{
    "id" : "60e0c5496d70aed082bc112d"
}
```
> Response
```
{
    "message": "Delete educational data succeed"
}
```
#### Put educational
`PUT localhost:8000/educational`

> BODY
```
{
    "id":"60e0d246ea0ae6cfe0081ea3",
    "data" : {
        "tahunajaran" :"2021",
        "tingkat":"SD"
    }
}
```
> Response
```
{
    "message": "educational data edited"
}
```
#### Post educational
`POST localhost:8000/educational`

> BODY
```
{"educational_id":"4", "tingkat": "SMA", "tahunajaran" : "2021"}
```
> Response
```
{
    "message": "educational data created"
}
```

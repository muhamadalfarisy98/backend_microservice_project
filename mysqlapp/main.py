from app import app

if __name__ == "__main__":
    app.run()

"""
@membuat database:
CREATE DATABASE school;

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
"""

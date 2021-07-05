from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
"""
@brief : inisiasi engine ORM untuk Tabel student
"""
engine = create_engine('mysql+mysqlconnector://root:enjoy66471@localhost:3306/school',echo = True)
Session = sessionmaker(bind = engine)
session = Session()

if session:
    print("Connection success")

# menginisiasi base class
Base = declarative_base()

#inherit base
class Student(Base):
    __tablename__ = 'student'
    siswa_id = Column(Integer, primary_key = True)
    username = Column(String)
    email = Column(String)
    namadepan = Column(String)
    namabelakang = Column(String)
    parent_id = Column(Integer, ForeignKey("parent.parent_id"))
    class_id = Column(Integer, ForeignKey("class.class_id"))

class Class(Base):
    __tablename__ = 'class'
    class_id = Column(Integer, primary_key = True)
    namakelas = Column(String)
    educational_id = Column(Integer)
    teacher_id = Column(Integer, ForeignKey("teacher.teacher_id"))
    seats = Column(Integer)

class Parent(Base):
    __tablename__ = 'parent'
    parent_id = Column(Integer, primary_key = True)
    username = Column(String)
    email = Column(String)
    nama = Column(String)
    phone = Column(String)

def showStudent():
    try:
        res = session.query(Student).all()
        data = []
        for row in res:
            row_data = {
                "id" : row.siswa_id,
                "username" : row.username,
                "email" : row.email,
                "namadepan" : row.namadepan,
                "namabelakang" : row.namabelakang,
                "parent": row.parent_id,
                "class_id": row.class_id,
            }
            data.append(row_data)
        return data

    except Exception as e:
        print(e)

def showStudentById(**params):
    res = session.query(Student).filter(Student.siswa_id == params['siswa_id']).one()
    data = {
                "id" : res.siswa_id,
                "username" : res.username,
                "email" : res.email,
                "namadepan" : res.namadepan,
                "namabelakang" : res.namabelakang,
                "parent_id": res.parent_id,
                "class_id": res.class_id,
    }
    return data

def insertStudent(**params) :
    """
    @contoh input:
    { data : {
            "username" : 'faris',
            "email" : 'faris@gmail.com',
            "namadepan" : 'faris',
            "namabelakang" : 'kudo',
            "parent_id": 1,
            "class_id": 1,
        }
    }
    """
    try:
        session.add(Student(**params['data']))
        session.commit()

    except Exception as e:
        print(e)


def updateStudentById(**params):
    """
    @input:
    params = {
        "siswa_id" : 1,
        "data" : {
            "username":"mijon",
            "namabelakang": "dll",
        }
    }
    """
    res = session.query(Student).filter(Student.siswa_id == params['siswa_id']).one()
    # res.namadepan = params['data'].get('namadepan','')
    res.namabelakang = params['data'].get('namabelakang','')
    # res.parent_id = params['data'].get('parent_id','')
    # res.class_id = params['data'].get('class_id','')
    try:
        session.commit()
    except Exception as e:
        print(e)
    message = "Siswa dengan Id {} berhasil diupdate".format(params['siswa_id'])
    data = {"message" : message}
    return data

def deleteStudentById(**params):
    res = session.query(Student).filter(Student.siswa_id == params['siswa_id']).one()
    session.delete(res)
    session.commit()
    message = "Siswa dengan Id {} berhasil dihapus".format(params['siswa_id'])
    data = {"message":message}
    return data

def showStudentByEmail(**params):
    res = session.query(Student).filter(Student.email == params['email']).one()
    data = {
                "username" : res.username,
                "email" : res.email
            }
    return data
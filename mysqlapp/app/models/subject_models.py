from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
"""
@brief : inisiasi engine ORM untuk Tabel subject
"""
engine = create_engine('mysql+mysqlconnector://root:enjoy66471@localhost:3306/school',echo = True)
Session = sessionmaker(bind = engine)
session = Session()

if session:
    print("Connection success")

# menginisiasi base class
Base = declarative_base()

#inherit base
class Subject(Base):
    __tablename__ = 'subject'
    subject_id = Column(Integer, primary_key = True)
    matapelajaran = Column(String)
    kode = Column(String)
    class_id = Column(Integer, ForeignKey("class.class_id"))

class Class(Base):
    __tablename__ = 'class'
    class_id = Column(Integer, primary_key = True)
    namakelas = Column(String)
    educational_id = Column(Integer)
    teacher_id = Column(Integer, ForeignKey("teacher.teacher_id"))
    seats = Column(Integer)

def showSubject():
    try:
        res = session.query(Subject).all()
        data = []
        for row in res:
            row_data = {
                "id" : row.subject_id,
                "matapelajaran" : row.matapelajaran,
                "kode_pelajaran" : row.kode,
                "class_id": row.class_id,
            }
            data.append(row_data)
        return data

    except Exception as e:
        print(e)

def showSubjectById(**params):
    res = session.query(Subject).filter(Subject.subject_id == params['subject_id']).one()
    data = {
                "id" : res.subject_id,
                "matapelajaran" : res.matapelajaran,
                "kode_pelajaran" : res.kode,
                "class_id": res.class_id,
            }
    return data

def insertSubject(**params) :
    """
    @contoh input:
    { "data" : {
            "matapelajaran" : "kalkulus",
            "kode_pelajaran" : "k003",
            "class_id": "1"
        }
    }
    """
    try:
        session.add(Subject(**params['data']))
        session.commit()

    except Exception as e:
        print(e)


def updateSubjectById(**params):
    """
    @input:
    params = {
        "subject_id" : 1,
        "data" : {
            "kode":"b00x",
            "matapelajaran": "fisika",
        }
    }
    """
    res = session.query(Subject).filter(Subject.subject_id == params['subject_id']).one()
    # res.matapelajaran = params['data'].get('matapelajaran','')
    res.kode = params['data'].get('kode','')
    try:
        session.commit()
    except Exception as e:
        print(e)
    message = "Subject dengan Id {} berhasil diupdate".format(params['subject_id'])
    data = {"message" : message}
    return data

def deleteSubjectById(**params):
    session.rollback()
    res = session.query(Subject).filter(Subject.subject_id == params['subject_id']).one()
    session.delete(res)
    session.commit()
    message = "subject dengan Id {} berhasil dihapus".format(params['subject_id'])
    data = {"message" : message}
    return data

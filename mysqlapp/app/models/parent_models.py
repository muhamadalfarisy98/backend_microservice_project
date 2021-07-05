from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
"""
@brief : inisiasi engine ORM untuk Tabel parent
"""
engine = create_engine('mysql+mysqlconnector://root:enjoy66471@localhost:3306/school',echo = True)
Session = sessionmaker(bind = engine)
session = Session()

if session:
    print("Connection success")

# menginisiasi base class
Base = declarative_base()

#inherit base
class Parent(Base):
    __tablename__ = 'parent'
    parent_id = Column(Integer, primary_key = True)
    username = Column(String)
    email = Column(String)
    nama = Column(String)
    phone = Column(String)


def insertParent(**params) :
    """
    @contoh input:
    { data : {
            "username" :'RK',
            "email" :'faris@gmail.com',
            "nama" : 'faris',
            'phone' : '0821312'
        }
    }
    """
    try:
        session.add(Parent(**params['data']))
        session.commit()

    except Exception as e:
        print(e)

def showParent():
    try:
        res = session.query(Parent).all()
        data = []
        for row in res:
            row_data = {
                "id" : row.parent_id,
                "username" : row.username,
                "email" : row.email,
                "nama" : row.nama,
                "phone": row.phone
            }
            data.append(row_data)
        return data

    except Exception as e:
        print(e)

def showParentById(**params):
    res = session.query(Parent).filter(Parent.parent_id == params['parent_id']).one()
    data = {
                "id" : res.parent_id,
                "username" : res.username,
                "email" : res.email,
                "nama" : res.nama,
                "phone": res.phone
        }
    return data

def updateParentById(**params):
    """
    @input:
    params = {
        "parent_id" : 3.
        "data" : {
            "username":"mijon",
            "phone": 9821312,
            "name": "dll",
        }
    }
    """
    res = session.query(Parent).filter(Parent.parent_id == params['parent_id']).one()
    # res.username = params['data'].get('username','')
    # res.email = params['data'].get('email','')
    res.phone = params['data'].get('phone','')
    res.nama = params['data'].get('nama','')
    try:
        session.commit()
    except Exception as e:
        print(e)
    message = "Parent dengan Id {} berhasil diupdate".format(params['parent_id'])
    data = {"message" : message}
    return data

def deleteParentById(**params):
    res = session.query(Parent).filter(Parent.parent_id == params['parent_id']).one()
    session.delete(res)
    session.commit()
    message = "Parent dengan Id {} berhasil dihapus".format(params['parent_id'])
    data = {"message":message}
    return data

def showParentByEmail(**params):
    res = session.query(Parent).filter(Parent.email == params['email']).one()
    data = {
                "username" : res.username,
                "email" : res.email
            }
    return data
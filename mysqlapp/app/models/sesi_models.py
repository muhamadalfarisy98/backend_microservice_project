from mysql.connector import connect
import datetime

class Database:
    def __init__(self):
        try:
            self.db = connect(
                            host = "localhost",
                            user = "root",
                            passwd = "enjoy66471",
                            database = "school"
                        )
        except Exception as e:
            print(e)

    def showSesi(self):
        try:
            cr = self.db.cursor()
            query = """
                select * from sesi;
            """
            cr.execute(query)
            data = cr.fetchall()
            return data
        except Exception as e:
            print(e)

    def insertSesi(self, **params):
        try:
            column = ', '.join(params['data'].keys())
            values = tuple(params['data'].values())
            crud_query = """
                insert into sesi
                    ({0}) 
                values 
                    {1};
                """.format(column, values)
            cr = self.db.cursor()
            cr.execute(crud_query)
            self.dataCommit()
            
        except Exception as e:
            print(e)
        
    def updateSesiById(self, **params):
        try :
            query = """
                update sesi
                set {0}
                where sesi_id = {1};
            """.format(self.restructureparams(**params['data']),params['sesi_id'])
            cr = self.db.cursor()
            cr.execute(query)
            self.dataCommit()

        except Exception as e:
            print(e)
        
    def deleteSesiById(self,**params):
        try:
            query = """
                delete from sesi
                where sesi_id = {};
                """.format(params['sesi_id'])
            cr = self.db.cursor()
            cr.execute(query)
            self.dataCommit()

        except Exception as e:
            print(e)

    def dataCommit(self):
        self.db.commit()

    def restructureparams(self, **data):
        lst = ['{0} = "{1}"'.format(key,val) for key,val in data.items()]
        res = ', '.join(lst)
        return res

    def closeConnection(self):
        if self.db is not None and self.db.is_connected():
            self.db.close()
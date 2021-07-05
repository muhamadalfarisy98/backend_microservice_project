from mysql.connector import connect

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

    def showJadwal(self):
        try:
            cr = self.db.cursor()
            query = """
                select * from jadwal;
            """
            cr.execute(query)
            data = cr.fetchall()
            return data
        except Exception as e:
            print(e)

    def showSesiJadwalById(self, **params):
        try:
            cr = self.db.cursor()
            query = """
                select 
                    s.*
                from
                    jadwal as j
                    inner join sesi as s on s.jadwal_id = j.jadwal_id
                where
                    j.jadwal_id = {}
                ;
            """.format(params['jadwal_id'])
            cr.execute(query)
            data = cr.fetchall()
            return data
            
        except Exception as e:
            print(e)

    def insertJadwal(self, **params):
        try:
            column = ', '.join(params['data'].keys())
            values = tuple(params['data'].values())
            crud_query = """
                insert into jadwal
                    ({0}) 
                values 
                    {1};
                """.format(column, values)
            cr = self.db.cursor()
            cr.execute(crud_query)
            self.dataCommit()
            
        except Exception as e:
            print(e)
        
    def updateJadwalById(self, **params):
        try :
            query = """
                update jadwal
                set {0}
                where jadwal_id = {1};
            """.format(self.restructureparams(**params['data']),params['jadwal_id'])
            cr = self.db.cursor()
            cr.execute(query)
            self.dataCommit()

        except Exception as e:
            print(e)
        
    def deleteJadwalById(self,**params):
        try:
            query = """
                delete from jadwal
                where jadwal_id = {};
                """.format(params['jadwal_id'])
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
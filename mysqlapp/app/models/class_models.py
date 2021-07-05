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

    def showClass(self):
        try:
            cr = self.db.cursor()
            query = """
                select * from class;
            """
            cr.execute(query)
            data = cr.fetchall()
            return data
        except Exception as e:
            print(e)

    def showStudentClassById(self, **params):
        try:
            cr = self.db.cursor()
            query = """
                select 
                    s.*
                from
                    student as s
                    inner join class as c on c.class_id = s.class_id
                where
                    c.class_id = {}
                ;
            """.format(params['class_id'])
            cr.execute(query)
            data = cr.fetchall()
            return data
        except Exception as e:
            print(e)

    def insertClass(self, **params):
        try:
            column = ', '.join(params['data'].keys())
            values = tuple(params['data'].values())
            crud_query = """
                insert into class
                    ({0}) 
                values 
                    {1};
                """.format(column, values)
            cr = self.db.cursor()
            cr.execute(crud_query)
            self.dataCommit()
            
        except Exception as e:
            print(e)
        
    def updateClassById(self, **params):
        try :
            query = """
                update class
                set {0}
                where class_id = {1};
            """.format(self.restructureparams(**params['data']),params['class_id'])
            cr = self.db.cursor()
            cr.execute(query)
            self.dataCommit()

        except Exception as e:
            print(e)
        
    def deleteClassById(self,**params):
        try:
            query = """
                delete from class
                where class_id = {};
                """.format(params['class_id'])
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
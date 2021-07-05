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

    def showTeacher(self):
        try:
            cr = self.db.cursor()
            query = """
                select * from teacher;
            """
            cr.execute(query)
            data = cr.fetchall()
            return data
        except Exception as e:
            print(e)

    def showTeacherById(self, **params):
        try:
            cr = self.db.cursor()
            query = """
                select * from teacher
                where teacher_id = {};
            """.format(params['teacher_id'])
            cr.execute(query)
            data = cr.fetchone()
            return data
        except Exception as e:
            print(e)
    
    def showTeacherByEmail(self,**params):
        try:
            cr = self.db.cursor()
            query = """
                select * from teacher
                where email = "{}";
            """.format(params["email"])
            cr.execute(query)
            data = cr.fetchone()
            return data
        except Exception as e:
            print(e)

    def insertTeacher(self, **params):
        try:
            column = ', '.join(params['data'].keys())
            values = tuple(params['data'].values())
            crud_query = """
                insert into teacher
                    ({0}) 
                values 
                    {1};
                """.format(column, values)
            cr = self.db.cursor()
            cr.execute(crud_query)
            self.dataCommit()
        except Exception as e:
            print(e)
        
    def updateTeacherById(self, **params):
        try :
            query = """
                update teacher
                set {0}
                where teacher_id = {1};
            """.format(self.restructureparams(**params['data']),params['teacher_id'])
            cr = self.db.cursor()
            cr.execute(query)
            self.dataCommit()
        except Exception as e:
            print(e)
        
    def deleteTeacherById(self,**params):
        try:
            query = """
                delete from teacher
                where teacher_id = {0};
                """.format(params['teacher_id'])
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
from pymongo import MongoClient
import logging
_logger = logging.getLogger(__name__)
import csv
from bson.objectid import ObjectId

class database():
    def __init__(self):
        try :
            self.nosql_db = MongoClient(host = 'localhost', port = 27017)
            self.db = self.nosql_db.school
            self.mongo_col = self.db.educational
            _logger.warning(' === Database connected ===')
        except Exception as e:
            print(e)
        pass

    def showEducational(self):
        """
        mencari dan return semua data
        """
        query = {}
        res = self.mongo_col.find(query)
        # return res
        out = [item for item in res]
        _logger.warning(' out : {}'.format(out))
        return out
    
    def showEducationalById(self, **params):
        """
        mencari dan melakukan
        return data dengan masukan idnya    
        """
        try :
            query = { 
                "_id": ObjectId(params["id"]) 
            } 
            res = self.mongo_col.find_one(query)
            return res
        except Exception as e:
            print(e)

    def insertEducational(self, document):
        self.mongo_col.insert_one(document)

    def updateEducationalById(self, **params):
        """
        @contoh_input:
        params = {
            "id": "xxxxx",
            "data: {...,...}
        }
        """
        query_1 = {"_id":ObjectId(params["id"])}
        query_2 = {"$set": params["data"]}
        self.mongo_col.update_one(query_1,query_2)

    def deleteEducationalById(self, **params):
        """
        menghapus educational berdasarkan input Id
        """
        query = { 
            "_id": ObjectId(params["id"]) 
        } 
        self.mongo_col.remove(query)

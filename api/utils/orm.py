from pymongo import MongoClient
from api.config.config import Config
from pymongo.errors import OperationFailure


class Database:
    
    def __init__(self):
        self.client = MongoClient(Config.url_database)
        self.db = self.client[Config.database]
    
    
    def get_collection(self, collection_name):
        return self.db[collection_name]

class ORM:
    
    def __init__(self):
        self.db = Database()
    

    def check_for_injection(self, collection_name):
        try:
            collection = self.db.get_collection(collection_name)
            collection.estimated_document_count()
        except OperationFailure:
            raise ValueError("Something seems to be wrong.")
        return collection

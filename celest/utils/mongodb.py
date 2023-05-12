from pymongo import MongoClient

from celest.config.config import Config


class Database:
    """
    Celest provides support for MongoDB database. The configurations are made directly in the 
    config/config.py file
    """
    
    def __init__(self):
        self.client = None
        self.db = None
        self.collection = None
        self.tokens_collection = None
    
    
    def connect(self):
        self.client = MongoClient(Config.url_database)
        self.db = self.client[Config.database]
        self.collection = self.db[Config.collection]
        self.tokens_collection = self.db[Config.token_collention]


    def create_user(self, user_data):
        if not self.client:
            self.connect()
        user = self.tokens_collection.insert_one(user_data).inserted_id
        return user


    def find_user(self, user_id):
        if not self.client:
            self.connect()
        user = self.tokens_collection.find_one({"_id": user_id})
        return user
    

    def update_user(self, user_id, new_data):
        if not self.client:
            self.connect()
        result = self.tokens_collection.update_one({"_id": user_id}, {"$set": new_data})
        return result


    def delete_user(self, user_id):
        if not self.client:
            self.connect()
        result = self.tokens_collection.delete_one({"_id": user_id})
        return result
    
    
    def register_token(self, token):
        if not self.client:
            self.connect()
        token_id = self.tokens_collection.insert_one(token).inserted_id
        return token_id
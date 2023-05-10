from jose import jwt
from pymongo import MongoClient

import datetime
from api.config.config import Config


class Database:
    
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


class Token:
    
    @staticmethod
    def generate_token(data: dict, secret_key: str = 'ai_ze_da_manga', expiration: int = 7200):
        now = datetime.datetime.utcnow()
        payload = {
            'sub': data['username'],
            'iss': 'Amino xD', # Enter your company
            'iat': int(now.timestamp()),
            'exp': int((now + datetime.timedelta(seconds=expiration)).timestamp()),
            **data
        }
        token = jwt.encode(claims=payload, algorithm='HS256', key=secret_key)
        if Config.mongodb_databse:
            db = Database()
            db.connect()
            db.register_token(token=token)
        return token
    
    
    @staticmethod
    def decrypt_token(token: str, secret_key: str):
        payload = jwt.decode(token, key=secret_key, algorithms=['HS256'])
        return payload
    
    
    @staticmethod
    def validate_token(token: str, secret_key: str):
        try:
            jwt.decode(token, key=secret_key, algorithms=['HS256'])
            return True
        except:
            return False

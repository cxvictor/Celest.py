from jose import jwt
import datetime

from celest.config.config import Config
from celest.utils.mongodb import Database

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

import jwt
import datetime

from user import User

class Token:
    
    @staticmethod
    def generate_token(entity: dict, secret_key: str, expiration: int = 7200):
        payload = {
            'sub': entity['username'],
            'iss': '',
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expiration),
            **entity
        }
        token = jwt.JWT().encode(payload=payload, key=secret_key, alg='HS256')
        return token
    
    #https://fusionauth.io/learn/expert-advice/tokens/jwt-components-explained


    
    @staticmethod
    def verify_token(token: str, secret_key: str):
        payload = jwt.JWT.decode(token, secret_key, algorithms=['HS256'])
        return payload
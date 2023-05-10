class User:
    def __init__(self, username: str = None, device_id: str or int = None, user_id: str or int = None):
        self.username = username
        self.device_id = device_id
        self.uid = user_id

    def headers_user(self):
        user_dict = {
            'username': self.username,
            'device_id': self.device_id,
            '_id': self.uid
        }
        
        return dict(filter(lambda user: user[1] is not None, user_dict.items()))

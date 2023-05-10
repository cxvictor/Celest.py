class User:
    def __init__(self, username: str = None, email: str = None, password: str = None, device_id: str or int = None, user_id: str or int = None):
        self.username = username
        self.email = email
        self.password = password
        self.device_id = device_id
        self.uid = user_id

    def headers_user(self):
        user_dict = {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'device_id': self.device_id,
            'uid': self.uid
        }
        
        return dict(filter(lambda user: user[1] is not None, user_dict.items()))

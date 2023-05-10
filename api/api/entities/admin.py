class Admin:
    def __init__(self, username: str = None, email: str = None, password: str = None, device_id: str or int = None, admin_id: str or int = None):
        self.username = username
        self.email = email
        self.password = password
        self.device_id = device_id
        self.admin_id = admin_id
        
        
    def headers_admin(self):
        admin_dict = {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'device_id': self.device_id,
            'uid': self.admin_id
        }
        
        return dict(filter(lambda adm: adm[1] is not None, admin_dict.items()))
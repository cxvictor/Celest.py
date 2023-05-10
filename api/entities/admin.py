class Admin:
    def __init__(self, username: str = None, device_id: str or int = None, admin_id: str or int = None):
        self.username = username
        self.device_id = device_id
        self.admin_id = admin_id
        
        
    def headers_admin(self):
        admin_dict = {
            'username': self.username,
            'device_id': self.device_id,
            '_id': self.admin_id
        }
        
        return dict(filter(lambda adm: adm[1] is not None, admin_dict.items()))
class User:
    def __init__(self, key: str or int = None, expiration: str = None, type: str = None, device: list = []):
        self.key = key
        self.expiration = expiration
        self.type = type
        self.device = device
        
    def headers_key(self):
        key_dict = {
            'key': self.key,
            'expiration': self.expiration,
            'type': self.type,
            'device': self.device
        }
        
        return dict(filter(lambda key: key[1] is not None and not isinstance(key[1], list), key_dict.items()))

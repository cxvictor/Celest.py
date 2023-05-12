
from datetime import datetime, timedelta

class DDoSException(Exception):
    Forbbiden = ("Unavailable service.")

class DDosProtection:
    """
    The DDosProtection class protects a server from DDoS attacks by limiting the number of requests
    per IP within a certain time frame, and if exceeded, the user is prevented from performing any 
    action when their action returns an exception. The limits are customizable.
    
    >>> REQUEST_LIMIT = 60
    >>> BAN_DURATION = 300
    
    `Change the two constants to configure your security 
    against DDoS attacks, and insert them into your route.`
    """
    
    REQUEST_LIMIT = 60
    BAN_DURATION = 300
    
    
    def __init__(self):
        self.requests = {}
        self.banned_ips = {}


    def limits(self, ip: str = None):
        """
        `Method responsible for checking requests based on the default settings inserted into the code`
        """
        now = datetime.now()
        
        if ip in self.banned_ips and self.banned_ips[ip] > now:
            raise DDoSException()

        
        requests = self.requests.get(ip, [])
        requests.append(now)
        self.requests[ip] = [request for request in requests if request > now - timedelta(seconds=60)]
        
        
        if len(self.requests[ip]) > self.REQUEST_LIMIT:
            self.banned_ips[ip] = now + timedelta(seconds=self.BAN_DURATION)
            self.banned_ips[ip] - now
            raise DDoSException()
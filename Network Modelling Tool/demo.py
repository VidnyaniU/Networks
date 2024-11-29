import ipaddress

class IPAddress:
    def __init__(self, ip):
        # Using ipaddress module to handle IP validation
        self.ip = ipaddress.ip_address(ip)
        
    def __str__(self):
        return str(self.ip)

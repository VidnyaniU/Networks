import ipaddress

class IPAddress:
    def __init__(self, ip):
        self.ip = ipaddress.ip_address(ip)
        
    def __str__(self):
        return str(self.ip)

class Device:
    def __init__(self, name):
        self.name = name
        self.interfaces = {}  # Mapping interface name to IP addresses
        
    def add_interface(self, interface_name, ip):
        self.interfaces[interface_name] = IPAddress(ip)
    
    def __str__(self):
        return f"Device: {self.name}, Interfaces: {self.interfaces}"

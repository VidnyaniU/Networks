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
    
    def get_ip(self, interface_name):
        # Return the IP address of a given interface
        return self.interfaces.get(interface_name, None)
    
class Subnet:
    def __init__(self, network, mask):
        self.network = ipaddress.ip_network(f"{network}/{mask}", strict=False)

    def __str__(self):
        return f"Subnet: {self.network}"

import socket

client_socket = socket.socket(socket.AF_INET  ,socket.SOCK_STREAM)

server_address = ("localhost" , 65432)

print("Connecting to ", server_address)
client_socket.connect(server_address)

try:
    #send message
    message = "Hello server!".encode()
    print("Sending:",message.decode())
    client_socket.sendall(message)

    #receive message
    data = client_socket.recv(1024) #bufsize = 1024
    print("Received :: ",data.decode())

finally:
    client_socket.close()

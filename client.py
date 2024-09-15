import socket

client_socket = socket.socket(socket.AF_INET  ,socket.SOCK_STREAM)

server_address = ("localhost" , 65432)

print("Connecting to ", server_address)
client_socket.connect(server_address)

try:
    #send message
    while True:
        message = input ("Enter the message ('bye' to exit) :: ")
        client_socket.sendall(message.encode())

        #receive message
        data = client_socket.recv(1024) #bufsize = 1024
        print("Received :: ",data.decode())

        if message.strip().lower() == "bye":
            print("Closing connection...")
            break

finally:
    client_socket.close()
    print("Connection closed!")

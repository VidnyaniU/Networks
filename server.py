import socket

#create a TCP/IP socket using the IPv4 addressing scheme
server_socket = socket.socket(socket.AF_INET  ,socket.SOCK_STREAM)
#AF_INET - IPv4 and AF_INET6 - IPv6
#SOCK_STREAM - TCP (Transmission Control Protocol), which provides reliable, connection-based communication. 
##It ensures that data is received in the same order it was sent, making it a stream-oriented protocol


#bind the socket to the address and port
server_address = ("localhost" , 65432)
server_socket.bind(server_address)

#listen from incoming connections
server_socket.listen(1)
print("Server is listening on" , server_address)

while True:
    print("Waiting for connection...")
    #to accept incoming connection request and save  client address
    connection , client_address = server_socket.accept()

    try:
        print("Connection from ",client_address)

        #receive the data in small chunks
        while True:
            data = connection.recv(1024)
            if data:
                print("Received :: ",data.decode())

                #send the same data back to the client 
                connection.sendall(data)
            
            else:
                break


    finally:
        #close the connection
        connection.close()
import socket 
import threading

# Function to handle incoming messages from the client
def handle_client(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg.lower() == 'quit':
                print("Client has disconnected.")
                break
            print(f"Received: {msg}")
        except OSError:
            print("Client has disconnected.")
            break
    client_socket.close()
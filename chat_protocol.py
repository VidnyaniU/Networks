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

# Function to start the server
def start_server(host='0.0.0.0', port=12345):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[+] Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

# Function to receive messages from the server in the client
def receive_messages(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg.lower() == 'quit':
                print("Server has disconnected.")
                break
            print(f"Received: {msg}")
        except OSError:
            print("Server has disconnected.")
            break

# Function to start the client
def start_client(host='127.0.0.1', port=12345):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    threading.Thread(target=receive_messages, args=(client,)).start()

    while True:
        msg = input("Enter message (type 'quit' to exit): ")
        client.send(msg.encode('utf-8'))
        if msg.lower() == 'quit':
            break

    client.close()

if __name__ == "__main__":
    choice = input("Type 'server' to start server or 'client' to start client: ").strip().lower()
    if choice == 'server':
        start_server()
    elif choice == 'client':
        ip_address = input("Enter server IP address: ").strip()  # Prompt for server IP
        start_client(host=ip_address)
    else:
        print("Invalid choice. Please type 'server' or 'client'.")
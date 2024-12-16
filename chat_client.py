import socket
import threading

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    def listen_for_messages():
        while True:
            try:
                data = client_socket.recv(1024).decode().strip()
                if not data:
                    continue
                print(f"Server: {data}")
                if data.lower() == "quit":
                    print("Server requested to close the connection.")
                    break
            except ConnectionResetError:
                print("Server disconnected.")
                break

    # Thread to listen for incoming messages from the server
    listener_thread = threading.Thread(target=listen_for_messages)
    listener_thread.start()

    # Client sending messages to the server
    while True:
        msg = input("Client: ")
        client_socket.sendall(msg.encode())
        if msg.lower() == "quit":
            print("Closing connection.")
            break

    # Clean up
    listener_thread.join()
    client_socket.close()
    print("Client closed.")

if __name__ == "__main__":
    host = "127.0.0.1"  # Server IP (localhost for testing, replace for remote)
    port = 12345        # Must match the server port
    start_client(host, port)

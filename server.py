import socket
import threading
from rsa_encryption import decrypt_key_with_rsa
from aes_encryption import decrypt

host = '127.0.0.1'
port = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print("Server is running and listening...")

clients = []

def handle_client(client_socket, address):
    print(f"Connected with {address}")

    # Step 1: Receive and decrypt AES key
    encrypted_aes_key = client_socket.recv(256)  # RSA encrypted data ~256 bytes
    aes_key = decrypt_key_with_rsa(encrypted_aes_key)

    # Step 2: Ask for name
    client_socket.send("Enter your name: ".encode('utf-8'))
    name = client_socket.recv(1024).decode('utf-8')
    welcome_msg = f"Hello {name}, you can now start chatting!"
    client_socket.send(welcome_msg.encode('utf-8'))

    while True:
        try:
            # Step 3: Receive encrypted message (in bytes) and decrypt
            encrypted_msg = client_socket.recv(1024)  # Receive as bytes, not string
            if not encrypted_msg:
                break

            # Decrypt the received encrypted message
            decrypted_msg = decrypt(encrypted_msg, aes_key)
            print(f"{name}: {decrypted_msg}")

            if decrypted_msg.lower() == 'exit':
                break

            # Optionally send a response back to the client
            client_socket.send("Message received".encode('utf-8'))

        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()
    print(f"{name} disconnected.")

while True:
    client_socket, address = server.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, address))
    thread.start()

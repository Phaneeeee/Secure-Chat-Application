import socket
import threading
import os
from aes_encryption import encrypt
from rsa_encryption import encrypt_key_with_rsa

host = '127.0.0.1'
port = 8888

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Step 1: Generate AES key (16 bytes)
aes_key = os.urandom(16)

# Step 2: Encrypt AES key using server's public RSA key
encrypted_aes_key = encrypt_key_with_rsa(aes_key)

# Step 3: Send encrypted AES key to the server
client.send(encrypted_aes_key)

# Step 4: Receive server's prompt: "Enter your name"
name_prompt = client.recv(1024).decode('utf-8')
print(name_prompt)

# Step 5: Enter and send your name
name = input()
client.send(name.encode('utf-8'))

# Step 6: Receive welcome message
welcome_message = client.recv(1024).decode('utf-8')
print(welcome_message)

# Step 7: Start chat loop (encrypting messages with AES)
while True:
    message = input("Enter message: ")

    # Encrypt message with AES key
    encrypted_message = encrypt(message, aes_key)
    client.send(encrypted_message)

    response = client.recv(1024).decode('utf-8')
    print("Message Sent")

    if message.lower() == 'exit':
        break

client.close()

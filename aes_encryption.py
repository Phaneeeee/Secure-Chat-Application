from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import os

# AES encryption function
def encrypt(message, aes_key):
    cipher = AES.new(aes_key, AES.MODE_CBC)  # CBC mode
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))  # Padding message
    iv = cipher.iv  # Store the IV to send it along with the ciphertext
    return iv + ct_bytes  # Prepend IV to the ciphertext for later use during decryption

# AES decryption function
def decrypt(encrypted_message, aes_key):
    iv = encrypted_message[:16]  # First 16 bytes are the IV
    ct = encrypted_message[16:]  # The rest is the ciphertext
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)  # Use the same IV to decrypt
    decrypted_message = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')  # Unpadding and decoding
    return decrypted_message

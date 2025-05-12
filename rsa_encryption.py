from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def load_public_key():
    with open("public.pem", "rb") as f:
        return RSA.import_key(f.read())

def load_private_key():
    with open("private.pem", "rb") as f:
        return RSA.import_key(f.read())

def encrypt_key_with_rsa(aes_key):
    public_key = load_public_key()
    cipher_rsa = PKCS1_OAEP.new(public_key)
    return cipher_rsa.encrypt(aes_key)

def decrypt_key_with_rsa(encrypted_key):
    private_key = load_private_key()
    cipher_rsa = PKCS1_OAEP.new(private_key)
    return cipher_rsa.decrypt(encrypted_key)

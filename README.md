# 🔐 Secure Chat Application using AES & RSA Encryption

This is a basic secure client-server chat application built with Python. It allows multiple clients to connect to a server and send encrypted messages using a hybrid encryption scheme (AES for messages, RSA for key exchange).

---

## 📌 Features

- Client-server communication over TCP
- AES encryption for chat messages
- RSA encryption for securely sharing AES key
- Simple command-line interface
- Multi-client support (one-way interaction with server)

---

## 🗂 Folder Structure

```
Secure-Chat-Application/
│
├── aes_encryption.py        # AES encryption/decryption functions
├── rsa_encryption.py        # RSA key loading & AES key encryption
├── client.py                # Client-side script
├── server.py                # Server-side script
├── private.pem              # Server's RSA private key
├── public.pem               # Server's RSA public key (used by client)
├── Project_Report.pdf       # Documentation explaining project details
└── __pycache__/             # Auto-generated Python bytecode files
```

---

## 🔧 Requirements

- Python 3.10+
- `pycryptodome` module

Install with:
```bash
pip install pycryptodome
```

---

## ▶️ How to Run

### 1. Start the Server
```bash
python server.py
```

### 2. Open One or More Clients (in different terminals)
```bash
python client.py
```

Each client:
- Sends its name to the server
- Starts sending encrypted messages
- Receives server acknowledgment

---

## 🔐 Encryption Process

- Client generates a random AES key.
- It encrypts this AES key using the server’s **RSA public key** (`public.pem`).
- Encrypted AES key is sent to the server.
- Server decrypts it using its **RSA private key** (`private.pem`).
- All future messages are encrypted using AES with that key.

---

## 🧪 Example Interaction

```
Client:
Enter your name:
Phanee
Hello Phanee, you can now start chatting!
Enter message: Hello, Server!
Message Sent

Server:
Connected with ('127.0.0.1', 56789)
Phanee: Hello, Server!
```

---

## 📄 License

This is a personal learning project developed by **Phaneendra Peravarapu**. Free to use, modify, and share.

---

## ✍️ Author

**Phaneendra Peravarapu**


from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt(message, key):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(message.encode()).decode()

def decrypt(encrypted_message, key):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_message.encode()).decode()

key = generate_key() 

email_address = "******@gmail.com"
email_password = "****************"
email_recipient = "***********.com.np"
encrypted_email_address = encrypt(email_address, key)
encrypted_email_password = encrypt(email_password, key)
encrypted_email_recipient = encrypt(email_recipient, key)

print("Encrypted Email Address:", encrypted_email_address)
print("Encrypted Email Password:", encrypted_email_password)
print("Encrypted Email Recipient:", encrypted_email_recipient)
#use this key in another file 
print("Encrypted key:", key)
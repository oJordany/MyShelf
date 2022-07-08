import json
from cryptography.fernet import Fernet
from controller.database import get_key, add_data_key, update_data_key


def encrypt():
    key1 = Fernet.generate_key()
    
    fernet1 = Fernet(key1)
    
    with open('confidential/confidential.txt', 'rb') as file:
        original1 = file.read()

    encrypted1 = fernet1.encrypt(original1)

    with open('confidential/confidential.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted1)

    key2 = Fernet.generate_key()
    
    add_data_key(key1, key2)

    fernet2 = Fernet(key2)
    
    with open('confidential/confidential.json', 'rb') as file:
        original2 = file.read()

    encrypted2 = fernet2.encrypt(original2)

    with open('confidential/confidential.json', 'wb') as encrypted_file:
        encrypted_file.write(encrypted2)

def updated_encryption():
    key2 = Fernet.generate_key()
    
    update_data_key(key2)

    fernet2 = Fernet(key2)
    
    with open('confidential/confidential.json', 'rb') as file:
        original2 = file.read()

    encrypted2 = fernet2.encrypt(original2)

    with open('confidential/confidential.json', 'wb') as encrypted_file:
        encrypted_file.write(encrypted2)

def decrypt(fileName, keyNumber):
    key = get_key(keyNumber)
    fernet = Fernet(key)

    with open(f'confidential/{fileName}', 'rb') as enc_file:
        encrypted = enc_file.read()
    
    decrypted = fernet.decrypt(encrypted)
    decrypted = decrypted.decode("utf-8") 

    datas = decrypted.split('\n')

    return datas

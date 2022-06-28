from cryptography.fernet import Fernet
from controller.database import get_key, add_data_key


def encrypt():
    key = Fernet.generate_key()
    
    add_data_key(key)

    fernet = Fernet(key)
    
    with open('confidential/confidential.txt', 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open('confidential/confidential.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt():
    key = get_key()
    fernet = Fernet(key)

    with open('confidential/confidential.txt', 'rb') as enc_file:
        encrypted = enc_file.read()
    
    decrypted = fernet.decrypt(encrypted)
    decrypted = decrypted.decode("utf-8") 

    datas = decrypted.split('\n')

    return datas
    
    
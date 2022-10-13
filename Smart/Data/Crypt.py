from cryptography.fernet import Fernet
from smartieJson import update
from smartieJson import read
def get_key():
    # key generation
    key = Fernet.generate_key()

    update("key", str(key))

def encode(string):
    key = read("key")
    byte_key = key.encode(encoding = 'UTF-8')
    fernet = Fernet(byte_key)
    
    encrypted = fernet.encrypt(string)
    return encrypted
    

def decode(string):
    key = read("key")
    
    fernet = Fernet(key)
    
    decrypted = fernet.decrypt(string)
    
    return decrypted

print(encode('deez nutz'))

print(decode(encode('deez nutz')))
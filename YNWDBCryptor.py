#===================================
#documentation code: py-uni-01-p/d
#by:R}AM#UN>

from Crypto.Cipher import AES
from Crypto import Random
import base64
from datetime import *

class Encryptor:    
        
    def pad(self, message_bytes):
        return message_bytes + b'\0' * (AES.block_size - len(message_bytes) % AES.block_size)
    
    def encrypt(self, key, message, key_size = 256):
        message = str(message)
        message_bytes = message.encode()          
        message_bytes = self.pad(message_bytes)
        #create a new random size key with an initialization vecotr
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message_bytes)
        
class Decryptor:
    
    def decrypt(self, key, encrypted_message):
        iv = encrypted_message[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        message_bytes = cipher.decrypt(encrypted_message[AES.block_size:])
        message_bytes = message_bytes.rstrip(b'\0')
        message = message_bytes.decode()
        return message

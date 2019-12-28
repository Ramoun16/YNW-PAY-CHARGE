from Crypto.Cipher import AES
from Crypto import Random
import base64
import os
from datetime import *
from YNWCommCryptor import *
from YNWServer import *

class Client:        
    
    def __init__(self):        
        self.key = Random.new().read(32)
        self.mr_e = Encryptor()
        self.mr_d = Decryptor()
        self.request = Request(self.key)
            
    def sendToServer(self, code):        
        message = str(code)
        
        client_side_encrypted_message = self.mr_e.encrypt(self.key, message)

        double_encrypted_message = self.request.encrypt(client_side_encrypted_message)
        
        server_side_encrypted_message = self.mr_d.decrypt(self.key, double_encrypted_message)

        self.request.decrypt(dobule_encrypted_message_decrypted_by_client)         
        
        #1- encrypt the number before sending to server
        #2- send number to server
        #3- wait for server response with a double key encrypted number
        #4- remove (dycrypt) my key
        #5- send back to server & wait for response message

    def checkCode(self, code):
        self.sendToServer(code)        
        return request.check() #msg that tells if code is :fabricated, expired, works
    

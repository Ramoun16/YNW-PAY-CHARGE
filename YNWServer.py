#===================================
#documentation code: py-uni-01-p/d
#by:R}AM#UN>

from Crypto.Cipher import AES
from Crypto import Random
import base64
from datetime import *
from YNWClient import *
from YNWDatabase import *
from YNWCode import *

class Request:

    def __init__(self, client_side_enc):
        self.key = Random.new().read(32)
        self.mr_e = Encryptor()
        self.mr_d = Decryptor()
        
    def encrypt(self, client_side_enccrypted_message):
        self.server_side_encrypted_message = self.mr_e.encrypt(self.key, client_side_enccrypted_message)

        return self.server_side_encrypted_message

    def decrypt(self, double_encrypted_message):
        original_message = self.mr_d.decrypt(self.key, double_encrypted_message)
        self.code = original_message
        
        
        #1- if server called: server should encypt the recieved message
        #2- send encypted message back to caller    
        #3- remove dycrypt my key    
        #send back to caller info about if msg existed b4 or not
    

    def check(self):
        if self.code in DB.db:
            if not expired(self.code.date):
                response = 'The process of charing {} LE was completed Sucessfully'                
            else:
                response = 'The chargin Code was expired, please try another valid code'                
        else:
            response = 'Sorry, The entered Code is fabricated.For charging issues call: 1616'

        return response


    def expired(self, code_date):
        today = date.today()
                
        if self.today > code_date:
            return True
        else:
            return False


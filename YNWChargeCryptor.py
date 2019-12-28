#===================================
#documentation code: py-uni-01-p/d
#by:R}AM#UN>

from random import *
from datetime import *
import pyffx
from YNWDatabase import *

class YNWCCEncryptor:
    '''encryption of values, dates, and stand_alone codes into one full encrypted YNWCC string'''
    
    #declaring encryptors for different parts of the full code including the full code itself
    date_cryptor = pyffx.String(b'YNW5gPlus', '1234567890', length = 2) 
    value_index_cryptor = pyffx.String(b'YNW5gPlus02', "0214357698", length = 1)
    stand_alone_code_cryptor = pyffx.String(b'YNWEgy02', '0123456789', length = 3)
    charge_code_cryptor = pyffx.String(b'YNWEGYPT2020', '1234567890',length = 16)
        
    def __init__(self, day, month, year, value_index, stand_alone_code):
        '''encrypting the 3 parts of the date (day,month,year), 
        the value, the 3 parts of the standalone code, and the full code itself'''
        
        #checkin' if number of digits match or not due to the encrpytor functions of pyffx
        self.__day_flag = False
        self.__month_flag = False
        if int(day) < 10:
            day = '0' + day
            self.__day_flag = True
        if int(month) < 10:
            month = '0' + month
            self.__month_flag = True
        
        #@#Encrypting the 3 parts of the date 
        self.__day_enc = YNWCCEncryptor.date_cryptor.encrypt(day)
        self.__month_enc = YNWCCEncryptor.date_cryptor.encrypt(month)
        self.__year_enc = YNWCCEncryptor.date_cryptor.encrypt(year)
        #@#== Date Encrypted ==#
        self.__date_enc = self.__day_enc + self.__month_enc + self.__year_enc
        
        #@#encrypting the value part
        #@#== Value Encrypted ==#
        self.__value_index_enc = YNWCCEncryptor.value_index_cryptor.encrypt(value_index)
        
        #slicing the stand_alone code into 3 parts
        self.__stand_alone_p1 = stand_alone_code[:3]
        self.__stand_alone_p2 = stand_alone_code[3:6]
        self.__stand_alone_p3 = stand_alone_code[6:]               
        
        #@#encrypting each part of the 3 parts of the stand_alone code
        self.__stand_alone_p1_enc = YNWCCEncryptor.stand_alone_code_cryptor.encrypt(self.__stand_alone_p1)
        self.__stand_alone_p2_enc = YNWCCEncryptor.stand_alone_code_cryptor.encrypt(self.__stand_alone_p2)
        self.__stand_alone_p3_enc = YNWCCEncryptor.stand_alone_code_cryptor.encrypt(self.__stand_alone_p3)
        
        #grouping the 3 encrypted parts of the stand_alone code
        #== Stand Alone Code Encrypted ==#
        self.__stand_alone_code_enc = self.__stand_alone_p1_enc + self.__stand_alone_p2_enc + self.__stand_alone_p3_enc        
        
        #grouping all 3 parts(date, value, stand alone code) of the full code
        self.__charge_code = self.__date_enc + self.__value_index_enc + self.__stand_alone_code_enc
        
        #@#== Full Code Encrypted ==#
        self.__charge_code_enc = YNWCCEncryptor.charge_code_cryptor.encrypt(self.__charge_code)
        
        # ==> proporties of the object <==                                
        self.charge_code_enc = self.__charge_code_enc                        
        
    def get_full_card_code_enc(self):
        return self.full_card_code_enc


class YNWCCDecryptor:
    '''decryption of encrypted card code into the originally generated
        full code with (day, month, year, value, stand_alone_code)'''
    
    values = DB.values
    
    #declaring encryptors for different parts of the full code including the full code itself
    date_cryptor = pyffx.String(b'YNW5gPlus', '1234567890', length = 2) 
    value_index_cryptor = pyffx.String(b'YNW5gPlus02', '0214357698', length = 1)
    stand_alone_code_cryptor = pyffx.String(b'YNWEgy02', '0123456789', length = 3)
    charge_code_cryptor = pyffx.String(b'YNWEGYPT2020', '1234567890',length = 16)
        
    def __init__(self, charge_code_enc):        
        '''decrypting the full card code into [3 parts of the date (day,month,year), 
        the value, the standalone code, and the full card code itself]'''
        
        #@#== Full Code Decrypted ==#
        self.__charge_code = YNWCCDecryptor.charge_code_cryptor.decrypt(charge_code_enc)
        
        #slicing all 3 parts(date, value, stand alone code) of the full_card_code_decrypted        
        self.__date_enc = self.__charge_code[:6]
        self.__value_index_enc = self.__charge_code[6]
        self.__stand_alone_code_enc = self.__charge_code[7:]
        
        #slicing the 3 encrypted parts of the stand_alone code                    
        self.__stand_alone_p1_enc = self.__stand_alone_code_enc[:3]        
        self.__stand_alone_p2_enc = self.__stand_alone_code_enc[3:6]        
        self.__stand_alone_p3_enc = self.__stand_alone_code_enc[6:]        
        
        #@#decrypting each part of the 3 parts of the stand_alone code
        #== Stand Alone Code Decrypted ==#
        self.__stand_alone_p1 = YNWCCDecryptor.stand_alone_code_cryptor.decrypt(self.__stand_alone_p1_enc)
        self.__stand_alone_p2 = YNWCCDecryptor.stand_alone_code_cryptor.decrypt(self.__stand_alone_p2_enc)
        self.__stand_alone_p3 = YNWCCDecryptor.stand_alone_code_cryptor.decrypt(self.__stand_alone_p3_enc)                
        
        #grouping the 3 parts of the stand_alone code into one part        
        self.__stand_alone_code = self.__stand_alone_p1 + self.__stand_alone_p2 + self.__stand_alone_p3
        
        #@#decrypting the value index part
        #@#== Value index Decrypted ==#
        self.__value_index = YNWCCDecryptor.value_index_cryptor.decrypt(self.__value_index_enc)
        
        #slicing the 3 parts of the encrypted date        
        self.__day_enc = self.__date_enc[:2]
        self.__month_enc = self.__date_enc[2:4]
        self.__year_enc = self.__date_enc[4:]
        
        #@#Decrypting the 3 parts of the date 
        #@#== Date Decrypted ==#
        self.__day = str(int(YNWCCDecryptor.date_cryptor.decrypt(self.__day_enc)))
        self.__month = str(int(YNWCCDecryptor.date_cryptor.decrypt(self.__month_enc)))
        self.__year = str(int(YNWCCDecryptor.date_cryptor.decrypt(self.__year_enc)))
        
        #P.S:there is no need to remove the leading zero in month or day because in the
        #last decryption of day and month a conersion to int was made
        
        # ==> proporties of the object <==                             
        self.day = self.__day #str 
        self.month = self.__month #str
        self.year = self.__year #str
        #expiration date in the integer form
        self.exp_date = (self.day) + (self.month) + (self.year)
        
        self.value_index = self.__value_index
        self.value = str(YNWCCDecryptor.values[int(self.value_index)])
        
        self.stand_alone_code = self.__stand_alone_code
        
        self.charge_code = self.exp_date + self.value_index + self.stand_alone_code
    
    def get_expiration_date(self):
        '''get expiration date in the date format'''
        __expiration_date = date(int('20' + str(self.year)), self.month, self.day)
        return (__expiration_date, 'date')        
             

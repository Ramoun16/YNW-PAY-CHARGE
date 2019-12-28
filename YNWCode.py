#===================================
#documentation code: py-uni-01-p/d
#by:R}AM#UN>

from datetime import *

class YNWCC:
    '''a data type for chargin codes
       conversion of any other datatype to chargingCode type is not posssible
       conversion of charging code is only limited to str while other datatypes are not allowed'''
    
    def __init__(self, date, value_index, stand_alone_code):
        '''takes the 3 parts of the ynwcc as parameters and convert them to a ynwcc'''

        self.date = date
        self.day = str(self.date.day)       
        self.month = str(self.date.month)
        self.year = str(self.date.year)[2:]
        
        self.value_index = value_index
        
        self.sacode = stand_alone_code
        
        self.__ynwcc = "{}{}{}{}{}".format(self.day,self.month,self.year[2:],self.value_index,self.sacode)
                
        #code is broke down into 3 main parts (type:code)
            #1- date: is also broke down into 3 parts (type:date)
                #i  - day (type:day)
                #ii - month(type:month)
                #iii- year(type:year)

            #2- value_index: (type:int)

            #3- stand_alone_code: (type:str)

        #defined as follow: code.date , code.value_index , code.stand_alone_code
        #code.date --> code.date.day, code.date.month, code.date.year
    
    def length(self):
        '''gets the length of ynwcc'''
        return len(self.__ynwcc)

    def __repr__(self):
        return self.__ynwcc
        
class YNWCCE:
    '''represents Any encrypted charging code'''

    def __init__(self, encrypted_code):
        '''convert any encrypted code string into an encrypted chargin code object'''
        self.YNWCCE = str(encrypted_code)
        
    def length(self):
        return len(self.YNWCCE)
        
    def __repr__(self):
        return self.YNWCCE

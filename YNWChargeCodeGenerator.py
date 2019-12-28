#===================================
#documentation code: py-uni-01-p/d
#by:R}AM#UN>

from random import *
from datetime import *
import pyffx
from YNWDatabase import *

class Generator:
    '''a class that generates a YNKCode.ChargingCode which consists of random expiration dates between 2 months,
       value for the card, and a stand alone code'''
    values = DB.values
    today = date.today()
    current_month = today.month
    
    def __init__(self, min_number_of_months, max_number_of_months):  
        '''initialization of the generators with range values'''
        self.min_number_of_days = 30 * min_number_of_months
        self.max_number_of_days = 30 * max_number_of_months        
        
    def generate(self):
        '''generation function of the generator'''
        #generate an expiration date, and value
        self.__generated_exp_day = randint(self.min_number_of_days, self.max_number_of_days)
        self.__generated_exp_date = Generator.today + timedelta(self.__generated_exp_day)
        self.__generated_value_index = Generator.values.index(choices(Generator.values, weights = [5, 6, 5, 4, 2, 2], k = 1)[0]) #for every 24 values 
        
        #gerantion of the stand_alone code
        while True:            
            self.__stand_alone_code = randint(100000000, 999999999)
            self.__stand_alone_code_group1 = str(self.__stand_alone_code)[:3]
            self.__stand_alone_code_group2 = str(self.__stand_alone_code)[3:6]
            self.__stand_alone_code_group3 = str(self.__stand_alone_code)[6:]
                        
            if int(self.__stand_alone_code_group2) != 0 : #and not self.__stand_alone_code_group2.startswith('0'):
                if int(self.__stand_alone_code_group3) != 0 : #and not self.__stand_alone_code_group3.startswith('0'):
                    break
        
        #creating properties for the generator with integer representations of 
        #different parts of the full code(day,month,year, value, stand alone code) - (inencrypted)
        # ==> proporties of the object <==
        self.day = str(self.__generated_exp_date.day) #str
        self.month = str(self.__generated_exp_date.month) #str
        self.year = str(self.__generated_exp_date.year)[:2] 
        #expiraion date in the string form
        self.exp_date = str(self.day) + str(self.month) + str(self.year)
        #expiration date in the date form
        self.date = date(int('20' + self.year), int(self.month), int(self.day))
        
        self.value_index = str(self.__generated_value_index) #str
        self.value = str(Generator.values[int(self.value_index)]) #str         
        
        self.stand_alone_code = str(self.__stand_alone_code)

        self.YNW_charge_code = self.exp_date + self.value_index + self.stand_alone_code                  
    
    def get_expiration_date(self):
        '''get expiration date in the date format'''
        return (self.__generated_exp_date, 'date')  
        

if __name__ == '__main__':
    gen = Generator(3, 8)
    gen.generate()
    print('day: ',gen.day)
    print('month: ',gen.month)
    print('year: ',gen.year)
    print('date: ', gen.date)
    print('value_index: ',gen.value_index)
    print('stand_alone_code: ',gen.stand_alone_code)
    print('length of stand_alone_code: ', len(gen.stand_alone_code))
    print('YNW_charge_code: ',gen.YNW_charge_code)
    print('length of YNWCC: ', len(gen.YNW_charge_code))
           

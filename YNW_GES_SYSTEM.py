from YNWChargeCodeGenerator import *
from YNWCode import *
from YNWChargeCryptor import *
import YNWDBCryptor 
from YNWDatabase import *
from Crypto import Random

#generating the charge code
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

#converting the generated charge code from str to YNWCC
ynwcc = YNWCC(gen.date, gen.value_index, gen.stand_alone_code)

#encrypting the ynwcc with YNWCipher
ynwcc_enc = YNWCCEncryptor(ynwcc.day, ynwcc.month, ynwcc.year, ynwcc.value_index, ynwcc.sacode)

#conversion of str ynwcc_enc to YNWCCE ynwcc_enc
ynwcce_enc = YNWCCE(ynwcc_enc)

#encrypting the ynwcce_enc before storing in the datebase
key = Random.new().read(32)
dbencryptor = YNWDBCryptor.Encryptor()
encrypted_yncwcce_enc = dbencryptor.encrypt(key, ynwcce_enc)

#storing to datebase
DB.codes.append(encrypted_yncwcce_enc)



    

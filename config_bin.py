from Crypto.Cipher import DES
from hashlib import md5

key = '\x47\x8D\xA5\x0B\xF9\xE3\xD2\xCF'
crypto = DES.new(key, DES.MODE_ECB)

#data = open('model.conf', 'rb').read()
#data_decrypted = crypto.decrypt(data[16:]).rstrip('\0')
#assert data[:16] == md5(data_decrypted).digest()
#open('model.conf.txt', 'wb').write(data_decrypted)

data = open('config.bin', 'rb').read()
data_decrypted = crypto.decrypt(data).rstrip('\0')
assert data_decrypted[:16] == md5(data_decrypted[16:]).digest()
open('config.bin.txt', 'wb').write(data_decrypted[16:])

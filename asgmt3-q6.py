#!/usr/bin/python

import sys, hashlib, binascii

data = str(sys.argv[1])
salt = 'Km5d5ivMy8iexuHcZrsD'

data = data.encode('utf-8')
salt = salt.encode('utf-8')


hash_value = hashlib.pbkdf2_hmac('sha512', data, salt, 200000)
output = binascii.hexlify(hash_value).decode()

print(output)

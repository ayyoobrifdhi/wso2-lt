#!/usr/bin/python

import sys, hashlib, binascii, secrets

data = str(sys.argv[1])
salt = secrets.token_hex(16)

data = data.encode('utf-8')
salt = salt.encode('utf-8')


hash_value = hashlib.pbkdf2_hmac('sha512', data, salt, 200000)
output = binascii.hexlify(hash_value).decode()

print(output)

#!/usr/bin/python

import sys, hashlib, binascii, secrets

data = str(sys.argv[1])
salt = secrets.token_hex(16)

data = data.encode('utf-8')
salt = salt.encode('utf-8')


output = hashlib.sha512(salt + data).hexdigest()

print(output)

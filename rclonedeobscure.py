#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
import sys
import base64

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

import code
import pprint

# Script version
VERSION = '1.1'

# Options definition
parser = argparse.ArgumentParser(description="version: " + VERSION)
options = parser.add_mutually_exclusive_group()
options.add_argument('-d', '--deobscure', help='Obscured/encrypted password to deobscure/decrypt', type = str)
options.add_argument('-o', '--obscure', help='Plain-text password to obscure/encrypt', type = str)

# Globals
# -- https://github.com/rclone/rclone/blob/master/fs/config/obscure/obscure.go
secret_key = b"\x9c\x93\x5b\x48\x73\x0a\x55\x4d\x6b\xfd\x7c\x63\xc8\x86\xa9\x2b\xd3\x90\x19\x8e\xb8\x12\x8a\xfb\xf4\xde\x16\x2b\x8b\x95\xf6\x38"

def base64_urlsafeencode(string):
    '''
    Removes any `=` used as padding from the encoded string.
    https://gist.github.com/cameronmaske/f520903ade824e4c30ab
    '''
    encoded = base64.urlsafe_b64encode(string)
    return encoded.decode('utf-8').rstrip("=")

def base64_urlsafedecode(string):
    '''
    Adds back in the required padding before decoding.
    https://gist.github.com/cameronmaske/f520903ade824e4c30ab
    '''
    padding = 4 - (len(string) % 4)
    string = string + ("=" * padding)
    return base64.urlsafe_b64decode(string)

def aes_ctr_encrypt(plaintext, iv):
    global secret_key
    
    crypter = AES.new(key=secret_key, mode=AES.MODE_CTR, initial_value=iv, nonce=b'')
    encrypted_password = crypter.encrypt(plaintext)
    
    return encrypted_password

def aes_ctr_decrypt(encrypted_password, iv):
    '''
    Do not forget to set an empty nonce
    https://stackoverflow.com/questions/56217725/openssh-opensshportable-which-key-should-i-extract-from-memory
    '''
    global secret_key
    crypter = AES.new(key=secret_key, mode=AES.MODE_CTR, initial_value=iv, nonce=b'')
    decrypted_password = crypter.decrypt(encrypted_password)
    
    return decrypted_password.decode('utf-8')

def deobscure(obscured):
    encrypted_password = base64_urlsafedecode(obscured)
    buf = encrypted_password[AES.block_size:]
    iv = encrypted_password[:AES.block_size]
    
    return aes_ctr_decrypt(buf, iv)

def obscure(plaintext):
    iv = get_random_bytes(AES.block_size)
    
    return base64_urlsafeencode(iv + aes_ctr_encrypt(str.encode(plaintext), iv))

def main():
    global parser
    options = parser.parse_args()
    
    if options.deobscure:
        print("[+] obscured password\t: %s" % options.deobscure)
        print("[+] deobscured password\t: %s" % deobscure(options.deobscure))
    
    if options.obscure:
        print("[+] plaintext password\t: %s" % options.obscure)
        print("[+] obscured password\t: %s" % obscure(options.obscure))
    
    return None

if __name__ == "__main__" :
    main()
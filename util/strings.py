# -*- coding: utf-8 -*-
import string
import random
import hashlib
import base64 as _base64
from Crypto.Cipher import AES as _AES
__author__ = 'myth'


def md5(a_str):
    """
    Calculate a string's md5.
    """

    return hashlib.md5(a_str).hexdigest()


def random_str(length):
    """
    Generate a given length random string.
    """

    return ''.join(random.sample(string.ascii_letters + string.digits, length))


def password_encrypt(password, secret):
    """
    Encrypt password by using md5 twice with a secret key.
    """

    return md5(md5(password) + secret)

_BLOCK_SIZE = 32
_PADDING = '{'

def encrypt_str(str, secret_key):
    """
    Encrypt a string using AES.
    :param str: string to encrypt.
    :type str: string
    :param secret_key, key use to encrypt.
    :type secret_key: string
    """

    # one-liner to sufficiently pad the text to be encrypted
    pad = lambda s: s + (_BLOCK_SIZE - len(s) % _BLOCK_SIZE) * _PADDING
    # one-liners to encrypt/encode and decrypt/decode a string
    # encrypt with AES, encode with base64
    aes_encode = lambda c, s: _base64.b64encode(c.encrypt(pad(s)))
    # create a cipher object using the random secret
    cipher = _AES.new(secret_key, _AES.MODE_ECB)

    return aes_encode(cipher, str)


def decrypt_str(str, secret_key):
    """
    Decrypt a string with AES.
    :param str: string to decrypt.
    :type str: string
    """

    # one-liners to encrypt/encode and decrypt/decode a string
    # encrypt with AES, encode with base64
    aes_decode = lambda c, e: c.decrypt(_base64.b64decode(e)).rstrip(_PADDING)
    # create a cipher object using the random secret
    cipher = _AES.new(secret_key, _AES.MODE_ECB)

    return aes_decode(cipher, str)
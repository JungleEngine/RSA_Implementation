from Crypto.Util import number as crypto
import numpy as np
import time
from sympy import mod_inverse
import random
from math import gcd
import matplotlib.pyplot as plt
from src.RSA_Attack import *

class Client():
    def __init__(self):
        self.n = None
        self.e = None
        self.d = None

    def encrypt_msg(self, msg):
        encrypted_data = [pow(ord(char), self.e, self.n) for char in msg]
        return encrypted_data

    def decrypt_msg(self, encrypted_data):
        decrypted_data = [pow(char, self.d, self.n) for char in encrypted_data]
        return decrypted_data


def generate_keys(n_bits):
    while True:
        p = crypto.getPrime(n_bits)
        q = crypto.getPrime(n_bits)
        if p != q:
            break

    n = p * q
    phi = (p - 1) * (q - 1)

    # Generate e.
    while True:
        e = random.getrandbits(n_bits) + 2
        g = gcd(e, phi)
        if g == 1:
            break

    d = mod_inverse(e, phi)
    return n, e, d


def test_RSA(msg, min_bits, max_bits):
    key_length_dec_time = []
    n_bits = min_bits
    while n_bits <= max_bits:
        n, e, d = generate_keys(n_bits)
        # Encrypt message with block size = 1 character.
        t_start = time.time()
        encrypted_data = [pow(ord(char), e, n) for char in msg]
        t_end = time.time()
        key_length_dec_time.append([n_bits, t_end - t_start])
        # Decrypted data.
        decrypted_data = "".join([chr(pow(char, d, n)) for char in encrypted_data])

        if (decrypted_data != msg):
            print("decrypted_data not equal to original message")

        n_bits = n_bits + 20
        print("current n_bits: ", n_bits)
    return key_length_dec_time


def test_brute_force_attack(msg, min_bits, max_bits):
    key_length = []
    key_length_dec_time = []
    while max_bits > min_bits:
        max_bits -= 1
        n_bits = max_bits
        n, e, d = generate_keys(n_bits)
        # Encrypt message with block size = 1 character.
        encrypted_data = [pow(ord(char), e, n) for char in msg]
        key_length.append(n_bits)
        # Decrypted data.
        t_start = time.time()
        decrypted_data = brute_force_attack(n, e, encrypted_data)
        t_end = time.time()

        key_length_dec_time.append([n_bits, t_end - t_start])
        if decrypted_data == msg:
            print("Success: Decrypted message: ", decrypted_data)
        else:
            print("Failed: Decrypted message: ", decrypted_data)
        decrypted_data = "".join([chr(pow(char, d, n)) for char in encrypted_data])
        if decrypted_data != msg:
            print("decrypted_data not equal to original message")

        print("current n_bits: ", n_bits)
    return key_length_dec_time


def attack_stats():
    msg = "h"
    key_length_dec_time = test_brute_force_attack(msg, min_bits=4, max_bits=28)

    key_length_dec_time.sort()
    x = [a for (a, b) in key_length_dec_time]
    y = [b for (a, b) in key_length_dec_time]
    plt.plot(x,y, linewidth=2.0)
    plt.ylabel('attack time')
    plt.xlabel('key_length')
    plt.show()


def encryption_stats():
    msg = "h"
    key_length_dec_time = test_RSA(msg, min_bits=4, max_bits=1024)

    key_length_dec_time.sort()
    x = [a for (a, b) in key_length_dec_time]
    y = [b for (a, b) in key_length_dec_time]
    plt.plot(x,y, linewidth=2.0)
    plt.ylabel('attack time')
    plt.xlabel('key_length')
    plt.show()

if __name__ == '__main__':
    msg = "hello"
    client_sender = Client()
    client_receiver = Client()
    n,e,d = generate_keys(16)

    client_sender.e = e
    client_sender.n = n

    client_receiver.d = d
    client_receiver.n = n
    client_receiver.e = e

    #############################################################
    #############################################################


    # Test RSA
    # encrypted_msg = client_sender.encrypt_msg(msg)
    # decrypted_msg = client_receiver.decrypt_msg(encrypted_msg)
    # decrypted_msg =  "".join([chr(char)for char in decrypted_msg])
    # if decrypted_msg == msg:
    #     print("Success: Decrypted message: ", decrypted_msg)
    # else:
    #     print("Failed: Decrypted message: ", decrypted_msg)

    #############################################################
    #############################################################


    # cipher_text
    # encrypted_msg = client_sender.encrypt_msg(msg)
    # decrypted_msg = chosen_cipher_attack(client_sender.n, client_sender.e, encrypted_msg, client_receiver)
    # decrypted_msg = "".join(decrypted_msg)
    # if decrypted_msg == msg:
    #     print("Success: Decrypted message: ", decrypted_msg)
    # else:
    #     print("Failed: Decrypted message: ", decrypted_msg)

#############################################################
#############################################################

    # Test Brute_force_attack
    # encrypted_msg = client_sender.encrypt_msg(msg)
    # decrypted_msg = brute_force_attack(client_sender.n, client_sender.e, encrypted_msg)
    # if decrypted_msg == msg:
    #     print("Success: Decrypted message: ", decrypted_msg)
    # else:
    #     print("Failed: Decrypted message: ", decrypted_msg)

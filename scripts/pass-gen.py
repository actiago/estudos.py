#!/usr/local/bin/python3.6
import random
import string

def randompassword(number):
    chars = random.sample(string.ascii_lowercase + string.digits, number)
    passw = ''.join(map(str, chars))
    return passw

amount = int(input("Quantas senhas:\n"))
number = int(input("Qual o comprimento da senha?\n"))
for i in range(amount):
    print(f"   Senha: {i} - {randompassword(number)} ")

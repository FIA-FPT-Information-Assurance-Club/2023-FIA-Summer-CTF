#!/usr/bin/python3

from Crypto.Util.number import getPrime, bytes_to_long
from math import lcm
import sys

def keygen():
    p = getPrime(1024)
    q = getPrime(1024)
    n1 = p*p*q
    n2 = p*q
    d = pow(n1,-1,lcm((p-1),(q-1)))
    return n1, n2, d

def encrypt(m):
    return pow(m,n1,n1)

def decrypt(c):
    return pow(c,d,n2)

def show_flag():
    with open('flag.txt') as f:
        flag = bytes_to_long(f.read().encode())
    print(f"{encrypt(flag) = }")
    sys.exit(0)

if __name__ == "__main__":
    print(sys.version)
    n1, n2, d = keygen()
    print(f"{n1 = }")
    print("""Actions
1) Encrypt
2) Decrypt
3) Show encrypted flag""")
    while True:
        choice = int(input("Enter action: "))
        match choice:
            case 1:
                m = int(input("m: ").strip())
                c = encrypt(m)
                print(c)
            case 2:
                c = int(input("c: ").strip())
                m = decrypt(c)
                print(m)
            case 3:
                show_flag()
            case _:
                show_flag()
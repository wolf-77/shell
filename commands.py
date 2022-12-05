# built in commands functions
import os
import secrets
import hashlib

def cls(*args):
    os.system('cls || clear')

def cd(*args):
    os.chdir(args[0][0])
    print(os.getcwd())

def pwd(*args):
    print(os.getcwd())

def ls(*args):
    for i in os.listdir(os.getcwd()):
        print(i)

def cat(*args):
    f = open(args[0][0], 'r')
    print(f.read())
    f.close()

def mfile(*args):
    # create new file in current directory
    f = open(args[0][0], 'w')
    f.close()
    print('New file created.')

def mkdir(*args):
    # create new directory in current directory
    os.mkdir(args[0][0])
    print('New directory created.')

def btc(*args):
    # generate bitcoin private keys
    bitcoin_private = secrets.randbits(256)
    hex_bitcoin_private = hex(bitcoin_private)
    private_key = hex_bitcoin_private[2:]
    print(f'private key :> {private_key}')

def hash(*args):
    # return hash of input
    h = hashlib.sha512(bytes(args[0][0], 'utf-8')).hexdigest()
    print(f'=> {args[0][0]} <hash 512> => {h}')

def env(*args):
    for i in os.getenv('PATH').split(';'):
        print(i)
from Crypto.PublicKey import RSA
import Crypto.Random
import binascii
from blockchain import Blockchain


class Wallet:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        try:
            with open('wallet.txt', mode='r') as f:
                keys = f.readline()
                public_key = keys[0][:-1]
                private_key = keys[1]
                self.public_key = public_key
                self.private_key = private_key
        except (IOError, IndexError):
            print('No wallet found')

    def create_key(self):
        private_key, public_key = self.generate_keys()
        self.private_key = private_key
        self.public_key = public_key
        try:
            with open('wallet.txt', mode='w') as f:
                f.write(public_key)
                f.write('\n')
                f.write(private_key)
        except (IOError, IndexError):
            print('Saving wallet failed.')

    def generate_keys(self):
        private_key = RSA.generate(1024, Crypto.Random.new().read)
        public_key = private_key.publickey()
        return binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'), binascii.hexlify(
            public_key.exportKey(format='DER')).decode('ascii')

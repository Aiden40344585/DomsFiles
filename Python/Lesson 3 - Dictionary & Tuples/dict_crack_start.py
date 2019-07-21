# Script:  dict_crack.py
# Description: Cracks password hash using a dictionary attack.
# Author:  Petra L & Rich McF
# Modified: Sept 2018
import sys
import hashlib

# list of passwords
dic = ['123','1234','12345','123456','1234567','12345678',
        'password', 'qwerty','abc','abcd','abc123','111111',
        'monkey','arsenal','letmein','trustno1','dragon',
        'baseball','superman','iloveyou','starwars',
        'montypython','cheese','123123','football','batman']

# create list of corresponding md5 hashes using a list comprehension
hashes = [None for pwd in dic] ### replace None with your formula

# zip dic and hashes to create a dictionary (rainbow table)
rainbow = {} ### replace empty dictionary with your formula


def dict_attack(passwd_hash):
    """Checks password hash against a dictionary of common passwords"""

    print (f'[*] Cracking hash: {passwd_hash}')

    
    passwd_found = None ### replace None with a look up using .get() on rainbow
        
    if passwd_found:
        print (f'[+] Password recovered: {passwd_found}')
    else:
        print (f'[-] Password not recovered')
                
def main():
    print('[dict_crack] Tests')
    passwd_hash = '4297f44b13955235245b2497399d7a93'
    dict_attack(passwd_hash)
    
if __name__ == '__main__':
	main()

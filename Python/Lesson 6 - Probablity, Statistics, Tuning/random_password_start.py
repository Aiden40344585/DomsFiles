# Script:  random_password.py
# Desc:    generates random password using secrets module
# Author:  Petra L
# Created: 28/9/17
#
# 

# something missing here
charset=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")     # explain
charset.extend([x.lower() for x in charset])   # explain
charset.extend(list("@&%_$#"))                 # explain
# add digits 0-9 to charset too

def generate_password(length):
    """add suitable function doc string here"""
    password=[]
    for n in range(length):
        password.append(secrets.choice(charset))
    # add suitable return statement

def main():
    # test cases
    pass

# boilerplate that calls main() if run as script
if __name__ == '__main__':
    main()


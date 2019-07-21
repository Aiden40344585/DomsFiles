# Script:  passwd_checker_start.py
# Desc:    Check strength of a password.
# Author:  Petra L, Rich Macf
# modified: Sept 2018

def check_strength(passwd):
    """checks the strength of a password"""
    # check password length
    if len(passwd) < 6:
        return False
        
    # check password for uppercase, lowercase and numeric chars
    hasupper = False;
    haslower = False;
    digitcount = 0;
    for c in passwd:
        #
        # add your code here
        # check whether c is upper case, lower case or numeric
        # and set corresponding variable to True or increment the counter
        #
        pass # remove this line
    if hasupper and haslower and digitcount>=3:
        return True    
                
def main():
    # ask user input. Could use PASWord123 and 123xY to test        
    # passwd = ''
    passwd = input('Enter your password to check its strength: ')
    # call strength checker function
    result = check_strength(passwd)
    # print the result
    if result: print (f'[*] Password {passwd} is strong')
    else: print(f'[*] Password {passwd} is NOT strong')
	
if __name__ == '__main__':
    main()

# Script: Manipulate Script Arguments
# Author: Rich Macf & Petra L
# Modified: Oct 2017
#
import sys

TRACE=True

def print_args(arg_list):
        '''print out the arguments passed in as a list'''
        print (f"[print_args] Args: {arg_list}")
  	
def main():
    print ('[print_args] Tests') 
    print_args(sys.argv)

# Standard boilerplate code to call the main() function to begin
# the program if run as a script.
if __name__ == '__main__':
    if TRACE: print ('[T] Module called as script, calling main()')
    main()
else:
    if TRACE: print ('[T] Module imported as library, not calling main')


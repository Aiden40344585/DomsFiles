# Script:   webpage_get.py
# Desc:     Fetches data from a webpage.
# Author:   PL & RM
# Modified: Oct 2018
#
import sys, urllib.request
        
def wget(url):
    ''' Retrieve a webpage via its url, and return its contents'''
    print ('[*] wget()')
    # open url like a file, based on url instead of filename
    webpage = None # ADD YOUR CODE TO OPEN URL HERE 
    # get webpage contents
    page_contents = None # ADD YOUR CODE HERE
    return page_contents

def main():
    # set test url argument
    sys.argv.append('http://www.napier.ac.uk/Pages/home.aspx')
    
    # Check args
    if len(sys.argv) != 2:
        print ('[-] Usage: webpage_get URL')
        return

    # Get web page
    print (wget(sys.argv[1]))

if __name__ == '__main__':
	main()

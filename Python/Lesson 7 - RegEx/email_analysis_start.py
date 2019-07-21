# Script:   email_analysis.py
# Desc:     extracts email addresses and IP numbers from a text file
#           or web page; for example, from a saved email header
# Author:   Petra Leimich Oct 2018
# 
# IMPORTANT: wget may fetch a byte object, but regex only works with strings
import sys, urllib.request, re
# import webpage_get #imports your own webpage_get module. 
        
# if you don't want to import your existing module, you need to define wget here:
"""def wget(url): 
    '''Suitable function doc string here'''
    # open url like a file, using url instead of filename
    # then get webpage contents and close
    # ... ADD YOUR CODE HERE ... 
    return page_contents"""

def txtget(filename):
    '''Suitable function doc string here'''
    # open file read-only, get file contents and close
    # ... ADD YOUR CODE HERE ... 
    return file_contents

def findIPv4(text):
    '''Suitable function doc string here'''
    ips = [] # ... ADD YOUR CODE HERE ...
    return ips

def findemail(text):
    '''Suitable function doc string here'''
    emails = [] # ... ADD YOUR CODE HERE ...
    return emails

def main():
    # url arguments for testing
    # un-comment one of the following 4 tests at a time
    #sys.argv.append('http://www.napier.ac.uk/Pages/home.aspx')
    sys.argv.append('http://asecuritysite.com/email01.txt')
    #sys.argv.append('http://asecuritysite.com/email02.txt')
    #sys.argv.append('email_sample.txt')
    # Check args
    if len(sys.argv) != 2:
        print ('[-] Usage: email_analysis URL/filename')
        return

    # Get and analyse web page
    try:
        # call wget() or txtget() as appropriate
        # ... ADD YOUR CODE HERE ...
        print ('[+] Analysing %s' % sys.argv[1])
        print ('[+] IP addresses found: ')
        # ... ADD YOUR CODE HERE ...
        print ('[+] email addresses found: ')
        # ... ADD YOUR CODE HERE ...
    except:
        # error trapping goes here
        pass # ... ADD YOUR CODE HERE ...                              

if __name__ == '__main__':
	main()

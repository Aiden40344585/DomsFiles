# Binary search for spell check

def binS(lo,hi,target):
    '''binary search for target in words.
       words must be declared elsewhere and a sorted list.'''
    if (lo>=hi):
        return False
    mid = (lo+hi) // 2
    piv = words[mid]
    if piv==target:
        return True
    if piv<target:
        return binS(mid+1,hi,target)
    return binS(lo,mid,target)


#Get a list of words
words = [s.strip("\n").lower() for s in open("words.txt")] 
words.sort() # sort the list
# tests
for w in ["accomodation","buchanan","macintosh","zebede"]:
    if not binS(0,len(words),w):
        print (w)
# Binary search for spell check

def binS(target, words):
    '''binary search for target in words. words must be a sorted list.'''
    def chop(lo,hi):
        if (lo>=hi):
            return False
        mid = (lo+hi) // 2
        piv = words[mid]
        if piv==target:
            return True
        if piv<target:
            return chop(mid+1,hi)
        return chop(lo,mid)
    return chop(0,len(words))

#Get a list of words
words = [s.strip("\n").lower() for s in open("words.txt")] 
words.sort() # sort the list
# tests
for w in ["accomodation","buchanan","macintosh","zebede"]:
    if not binS(w, words):
        print (w)

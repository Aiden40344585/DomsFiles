# linear search for spell check

def linS(target, words):
    '''linear search for target in words. words need not be sorted'''
    for s in words:
        if s==target:
            return True
    return False

#Get a list of words
words = [s.strip("\n").lower() for s in open("words.txt")] 
# tests
for w in ["accomodation","buchanan","macintosh","zebede"]:
    if not linS(w, words):
        print (w)
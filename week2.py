#Test: last element, first element, multiple elements, all
def remove(enteredlist, number):
    """removes all numbers in the list smaller than number""" 
    for i in range(len(enteredlist)-1, -1,-1):
        if enteredlist[i] < number:
            enteredlist.pop(i)

def copyElementsUnder(alist, number):
    """Returns a copy of the list, removing elements under number"""
    return [i for i in alist if i < number]

def removeByList(lst, collection):
    """Removes all elelements in the list that are in collection"""
    for i in collection:
        while i in lst:
            lst.remove(i)

def removeDuplicates(collection):
    """Returns a copy of the list with duplicates removed"""
    copy = list(set(collection))
    copy.sort()
    return copy

def listOverlap(collection1, collection2):
    """Returns the a list of the overlap of two colletions"""
    return [i for i in collection1 if i in collection2]

def listOverlap2(collection1, collection2):
    """Returns the a list of the overlap of two colletions"""
    result = []
    for i in collection1:
        if i in collection2:
            result.append(i)
    return result

def createList(start, stop, step):
    """Creates a list of numbers ranging from start to stop, with step spaces betwee"""
    return [i for i in range(start, stop, step)]

def clubEntry(name, guestlist):
    """Returns True if name is on the guestlist and True, False if not on or listed as False"""
    if not name in guestlist or guestlist[name] == False:
        return False
    else:
        return True

def factorial(number):
    """Returns the factorial of the number, or False if it has no factorial"""
    if number < 0:
        return False
    elif number == 0:
        return 1
    else:
        return number * factorial(number-1)

def fibSequence(number):
   """Returns a list of the fibonnaci sequence up to the position of number"""
   if number < 0:
       return False
   elif number == 0:
       return [1]
   elif number == 1:
       return[1,1]
   else:
        result = fibSequence(number-1)
        result.append(result[-1]+result[-2])
        return result

def hanoi(number):
    """returns the minimum number of steps needed to complete the towers of hanoi for n pieces"""
    if number <= 0:
        return False
    elif number == 1:
        return 1
    else:
        return hanoi(number-1)*2 + 1

def infiniteRecursion(number):
    """Will return the maximum level of recursion. Number should start at 0"""
    try:
        infiniteRecursion(number+1)
    except RuntimeError:
        print("Max Recursion:",number)

def encode(string):
    """Will return an encoded string"""
    codemap = {"a": "00",  
               "b": "01",
               "c": "02",
               "d": "03",
               "e": "04",
               "f": "05",
               "g": "06",
               "h": "07",
               "i": "08",
               "j": "09",
               "k": "10"}

    string = string.lower()
    codelist = [codemap[i] for i in string]
    string = ""
    for i in codelist:
        string += i
    return string

def decode(string):
    """Will return a decoded string"""
    codemap = {0: "a",
               1: "b",
               2: "c",
               3: "d",
               4: "e",
               5: "f",
               6: "g",
               7: "h",
               8: "i",
               9: "j",
               10: "k"}

    if len(string) < 2:
        return False
    if len(string) == 2:
        return codemap[int(string)]
    else:
        return codemap[int(string[0:2])] + decode(string[2:])

def encrypt(word, encryptionkey):
    word = encode(word)
    result = ""
    keypointer = 0
    for i in range(0, len(word), 2):
        if keypointer > len(encryptionkey):
            keypointer = 0
        token = str(int(word(i,i+2)) + encryptionkey(keypointer))
        if len(token) < 1:
            token = "0"+token
        result += token
    return result

def paperSize(string):
    if validpapersize(string):
         if string == "A0":
             return 841, 1189
         elif string[1] == 0:
             smallshort, smalllong = paperSize("A"+string[2:])
             return smalllong, smarllshort*2
         else: 
             anumber = int(string[1:0])
             smallshort, smalllong = paperSize("A"+str(anumber-1))
             return smalllong/2 , smallshort         

def validpapersize(string):
    """Returns True if a valid papersize, false otherwse"""
    if string[0] != "A" or string[1] != "0":
        return False
    elif string[1] == "0":
        for i in string[1:]:
            if i != "0":
                return False
        return True
    else:
       for i in string[1:]:
            if i not in string.digits:
                return False
       return True


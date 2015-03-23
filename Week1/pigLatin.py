VOWELS = "aeiouy" #This should really be a list or tuple but we've not see them yet

def isVowel(character):
    '''Returns True if the character is a vowel (y inclusive)'''
    character = character.lower()
    for i in VOWELS:
        if i == character:
            return True
    return False
# A better way to do this would be (again not seen these yet)   
#    if character.lower() in VOWELS:
#        return True
#    else:
#        return False
#

def allVowels(word):
    for i in word:
          if not isVowel(i):
            return False
    return True

def getPrefix(word):
    '''Returns a lowercase substring up to the first vowel (not inclusive) in the word'''
    prefix = ""
    word = word.lower()
    for i in word:
        if isVowel(i):
            return prefix
        else:
            prefix += i
    return prefix
            
def getStem(word):
    '''Returns a lowercase substring from the first vowel(inclusive) to the end'''
    return word[len(getPrefix(word)):].lower()

def translateWord(word):
    '''Translates a single word into Pig Latin'''
    #returns empty word
    if len(word) == 0:
        return ""
    
    #Sticks prefix and Stem together.
    #If word has no vowels, stem will be empty, so this works
    result = (getStem(word)+getPrefix(word)).lower()

    #Adds the different ending
    if allVowels(word):
        result += "yay"
    else:
        result += "ay"
    #Handles capitalisation   
    if word[0] == word[0].upper():
        result = result[0].upper()+ result[1:]
    return result
           
def getWord(sentence):
    '''Returns the first word up to the first non-alpha numeric character'''
    word = ""
    for i in sentence:
        if i.isalpha():
            word += i
        else:
            break
    return word

def translateSentence(sentence):
    '''Translates a sentence into Pig Latin'''

    result = ""
    #Gets non alpha-numeric characters and addes to the result as these must be preserved
    if len(sentence) == 0:
        return result    
    for i in sentence:
        if not i.isalpha():
            result += i
        else:
            break
    word = getWord(sentence[len(result):])
    start = len(word) + len(result) #point to resume parsing from
    result += translateWord(word)
    return result + translateSentence(sentence[start:])

#Test code
print(translateSentence("A funny jarring Apple structure"))
print(translateSentence("Funny jarring Apple! Structure?"))

# coding=UTF-8

'''
Created on 10.04.2012

@author: andreasrettig
'''
import random
from pprint import pprint
from string import lower
from de.dictionaryAnalyze import findSimilarWords, findWrongCharacters, reduceDecodeTable



def countLetters(text):
    letterCount = dict()

    for ch in (range(ord('a'),ord('z')+1)):
        letterCount[chr(ch)] = text.count(chr(ch))
    
    return letterCount

def toLowerCase(text):
    return ''.join(e for e in text if e.isalpha() or e == " ").lower()

frequencies = {
        'a': 6.51,
        'b': 1.89,
        'c': 3.06,
        'd': 5.08,
        'e': 17.40,
        'f': 1.66,
        'g': 3.01,
        'h': 4.76,
        'i': 7.55,
        'j': 0.27,
        'k': 1.21,
        'l': 3.44,
        'm': 2.53,
        'n': 9.78,
        'o': 2.51,
        'p': 0.79,
        'q': 0.02,
        'r': 7.00,
        's': 7.27,
        't': 6.15,
        'u': 4.35,
        'v': 0.67,
        'w': 1.89,
        'x': 0.03,
        'y': 0.04,
        'z': 1.13
    }
alpha = map(chr,range(ord('a'),ord('z')+1))

phrase = open("../finnland.txt",'r').read();
phrase = toLowerCase(phrase)
print phrase

#------
letterCount = countLetters(toLowerCase(open("../parforce.txt",'r').read()))
#frequenciesSorted = sorted(frequencies,key=frequencies.get,reverse=True);
frequenciesSorted = sorted(letterCount, key=letterCount.get, reverse=True)
#------

shuffled = alpha[:]
random.shuffle(shuffled)
decodeTable = dict(zip(alpha,shuffled))
decodeTable[' '] = ' '

crypted = map(decodeTable.get,phrase)
cryptedTxt="".join(crypted)

letterCount = countLetters(crypted)
cryptedFrequencies = sorted(letterCount, key=letterCount.get, reverse=True)

decodeTable = dict(zip(cryptedFrequencies,frequenciesSorted))
decodeTable[' '] = ' '

decrypted = map(decodeTable.get,cryptedTxt)
decryptedTxt="".join(decrypted)

print "Crypted"
print cryptedTxt[0:1000]
print "Decrypted"
print decryptedTxt[0:1000]

dictionaryfile = open('../ngerman.txt', 'r')
dictionary = set(lower(dictionaryfile.read()).split("\n"))
dictionaryfile.close()

dictionaryLen = dict()
for word in dictionary:
    length = len(word)
    if not (dictionaryLen.has_key(length)):
        dictionaryLen[length] = []
    dictionaryLen[length].append(word)
  
#-----------
exchangeTable = dict()
matchedWords = 0

for word in decryptedTxt.split(" "):
    if (len(word)>3):
        wordsWithLength = dictionaryLen[len(word)]
        similarWords = findSimilarWords(wordsWithLength,word)

        if (len(similarWords)<3) and (len(similarWords)>0):
            for similarWord in similarWords:
                findWrongCharacters(word, similarWord, exchangeTable)
                print word+" is similar to "+str(similarWord)
            print matchedWords
            if (matchedWords>70): break
            matchedWords+=1

reducedTable = reduceDecodeTable(exchangeTable)
pprint (exchangeTable)
print reducedTable
print decryptedTxt[0:1000]
#------------------

newDec = ""
for char in decryptedTxt:
    if (reducedTable.has_key(char)):
        newDec += reducedTable[char]
    else:
        newDec += char    
    
print newDec[0:1000]
#decodeTable = updateDecodeTable(decodeTable, reduceDecodeTable(exchangeTable))    
#decrypted = map(decodeTable.get,cryptedTxt)
#print ("".join(decrypted))
    
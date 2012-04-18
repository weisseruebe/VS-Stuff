# coding=UTF-8

'''
Created on 10.04.2012

@author: andreasrettig
'''
import random
import dictionaryAnalyze
from pprint import pprint
from string import lower

from de.dictionaryAnalyze import findSimilarWords, findWrongCharacters,\
    reduceDecodeTable, updateDecodeTable

def countLetters(text):
    letterCount = dict()

    for ch in (range(ord('a'),ord('z')+1)):
        letterCount[chr(ch)] = text.count(chr(ch))
    
    return letterCount

def toLowerCase(text):
    #delete_table = string.maketrans(string.ascii_lowercase + " " , ' ' * (len(string.ascii_lowercase)+1))
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

#print "Code table"
#print decodeTable
#print "Letter count"
#print letterCount
#print "Crypted sorted"
#print cryptedFrequencies
#print frequenciesSorted
print "Crypted"
print cryptedTxt
print "Decrypted"
print decryptedTxt

dictionaryfile = open('../ngerman.txt', 'r')
dictionary = set(lower(dictionaryfile.read()).split("\n"))
dictionaryfile.close()

dictionaryLen = dict()
for word in dictionary:
    length = len(word)
    if not (dictionaryLen.has_key(length)):
        dictionaryLen[length] = []
    dictionaryLen[length].append(word)
    
exchangeTable = dict()
rounds = 0

for word in decryptedTxt.split(" "):
    print "Searching "+word
    #similarWords = findSimilarWords(dictionary,word)
    if (len(word)>0):
        wordsWithLength = dictionaryLen[len(word)]
        similarWords = findSimilarWords(wordsWithLength,word)

        print word+" is similar to "+str(similarWords)
        """Nur eindeutige Treffer"""
        if (len(similarWords)==1):
            for similarWord in similarWords:
                findWrongCharacters(similarWord, word, exchangeTable)
                pprint (exchangeTable)
                pprint (reduceDecodeTable(exchangeTable))
             
            print rounds
            if (rounds>10): break
            rounds+=1
    
decodeTable = updateDecodeTable(decodeTable, reduceDecodeTable(exchangeTable))    
decrypted = map(decodeTable.get,cryptedTxt)
print "".join(decrypted)
    
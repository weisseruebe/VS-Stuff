'''
Created on 10.04.2012

@author: andreasrettig
'''
import random
import string
import sys
from idlelib.textView import textFile

def countLetters(text):
    letterCount = dict()

    for ch in (range(ord('a'),ord('z')+1)):
        letterCount[chr(ch)] = text.count(chr(ch))
    
    return letterCount

def toLowerCase(text):
    delete_table  = string.maketrans(string.ascii_lowercase, ' ' * len(string.ascii_lowercase))
    return text.lower().translate(None,delete_table);

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

frequenciesSorted = sorted(frequencies,key=frequencies.get,reverse=True);
phrase = open("",'r').read();
alpha = map(chr,range(ord('a'),ord('z')+1))

shuffled = alpha[:]
random.shuffle(shuffled)
codeTable = dict(zip(alpha,shuffled))

crypted = map(codeTable.get,phrase)

letterCount = countLetters(crypted)
cryptedFrequencies = sorted(letterCount, key=letterCount.get, reverse=True)

cryptedTxt="".join(crypted)
decodeTable = dict(zip(cryptedFrequencies,frequenciesSorted))
print cryptedTxt
decrypted = map(decodeTable.get,cryptedTxt)


print "Code table"
print codeTable
print "Letter count"
print letterCount
print "Crypted sorted"
print cryptedFrequencies
print frequenciesSorted
print "Decrypted"
print decrypted

'''
Created on 10.04.2012

@author: andreasrettig
'''

""" Return the key of dictionary dic given the value"""
def findKey(dic, val):
    return [k for k, v in dic.iteritems() if v == val][0]

""" Creates a dictionary with the letters to be exchanged and their probablity """
def findWrongCharacters(decString, origString, charList):
    index = 0
    while index < len(decString):
        if decString[index] != origString[index]:
            wrongChar = decString[index]
            rightChar = origString[index]
            if not (wrongChar in charList):
                charList[wrongChar] = dict()
                               
            if not (rightChar in charList[wrongChar]):
                charList[wrongChar][rightChar] = 1
            else:  
                charList[wrongChar][rightChar] += 1
        
        index += 1

""" Reduces the updateTable values to the one with the most occurencies"""
def reduceDecodeTable(updateTable, minOccurencies):
    exchangeTable = dict()
    for char in updateTable:
        charDict = updateTable[char]
        largestChar = max(charDict, key=charDict.get)
        if (charDict[largestChar] >= minOccurencies): 
            exchangeTable[char] = largestChar
    return exchangeTable

""" Changes the decoded letter in the codetable to the one in the updatetable 
that is given under its key """
def updateDecodeTable(decodeTable, updateTable):
    for key, value in decodeTable.items():
        if value in updateTable.keys():
            decodeTable[key] = updateTable[value]
            print value+" -> "+updateTable[value]
    return decodeTable

""" Checks if string1 can be converted to string2 by character substitution 
    and how similar the strings are 
    Return value 0 means: The Strings have a different pattern and / or no matching characters
    Return values > 0: The percentage of characters that match """    
def patternMatch(string1, string2):
    if not (len(string1) == len(string2)): return 0
    index = 0
    identicalChars = 0
    while index < len(string1):   
        c1 = string1[index]
        indices1 = [i for i, x in enumerate(string1) if x == c1]
        
        c2 = string2[index]
        indices2 = [i for i, x in enumerate(string2) if x == c2]
               
        if not (indices1 == indices2): return 0
        if c1 == c2:
            identicalChars += 1
            
        index += 1
    return identicalChars/float(len(string1))
 
"""Finds words in the dictionary that are similar to the given word"""       
def findSimilarWords(dictionary, word, minWordSimilarity):
    similarWords = []
    for dictWord in dictionary:
        sim = patternMatch(word, dictWord)
        if sim > minWordSimilarity and sim < 1:
            similarWords.append(dictWord)
    return similarWords
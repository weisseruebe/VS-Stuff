'''
Created on 10.04.2012

@author: andreasrettig
'''


""" Return the key of dictionary dic given the value"""
def find_key(dic, val):
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
def reduceDecodeTable(updateTable):
    exchangeTable = dict()
    for char in updateTable:
        charDict = updateTable[char]
        exchangeTable[char] = max(charDict, key=charDict.get)
    return exchangeTable

""" Changes the decoded letter in the codetable to the one in the updatetable 
that is given under its key """
def updateDecodeTable(decodeTable, updateTable):
    for char in updateTable:
        if char in decodeTable.values():
            key = find_key(decodeTable,char)
            decodeTable[key] = updateTable[char]
            print char+" -> "+decodeTable[key]
    return decodeTable

if __name__ == '__main__':
    exchangeTable = dict()
    findWrongCharacters("hillp","hallo",exchangeTable)
    findWrongCharacters("bauv","baum",exchangeTable)

    print exchangeTable

    decodeTable = dict()
    decodeTable['h'] = 'h'
    decodeTable['k'] = 'i'
    decodeTable['l'] = 'l'
    decodeTable['m'] = 'p'
    decodeTable['s'] = 't'
    decodeTable['r'] = 'v'

    print decodeTable
    reduced = reduceDecodeTable(exchangeTable)
    print updateDecodeTable(decodeTable, reduced) 
    
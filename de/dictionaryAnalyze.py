'''
Created on 10.04.2012

@author: andreasrettig
'''

decWord = "hillp"
dicWord = "hallo"

def find_key(dic, val):
    """return the key of dictionary dic given the value"""
    return [k for k, v in dic.iteritems() if v == val][0]

def findWrongCharacters(decString, origString):
    charList = dict()
    index = 0
    while index < len(decWord):
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
    return charList
    
def reduceDecryptTable(updateTable):
    newTable = dict()
    for char in updateTable:
        charDict = updateTable[char]
        newTable[char] = max(charDict, key=charDict.get)
    return newTable

#Change the wrong output chars
def updateCodeTable(codeTable, updateTable):
    for char in updateTable:
        print char
        if char in codeTable.values():
            key = find_key(codeTable,char)
            codeTable[key] = updateTable[char]
            print char+" -> "+codeTable[key]
    return codeTable

if __name__ == '__main__':
    newTable = findWrongCharacters(decWord,dicWord)
    codeTable = dict()
    codeTable['h'] = 'h'
    codeTable['k'] = 'i'
    codeTable['l'] = 'l'
    codeTable['m'] = 'p'

    print codeTable
    reduced = reduceDecryptTable(newTable)
    print updateCodeTable(codeTable, reduced) 
    #print newTable
    
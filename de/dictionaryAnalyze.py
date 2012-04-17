'''
Created on 10.04.2012

@author: andreasrettig
'''

decWord = "Hbllpppi"
dicWord = "Halloomo"


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
    
def reduceDecryptTable(table, updateTable):
    newTable = dict()
    for char in updateTable:
        charDict = updateTable[char]
        newTable[char] = max(charDict, key=charDict.get)
    return newTable

if __name__ == '__main__':
    newTable = findWrongCharacters(decWord,dicWord)
    codeTable = dict()
    codeTable['a'] = 'z'
    codeTable['z'] = 'a'
    print newTable
    print reduceDecryptTable(codeTable, newTable)
    #print newTable
    
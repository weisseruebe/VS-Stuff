'''
Created on 10.04.2012

@author: andreasrettig
'''

decWord = "Hbllpppi"
dicWord = "Hallommo"

charList = dict()

def matchCharacters():
    index = 0
    while index < len(decWord):
        if decWord[index] != dicWord[index]:
            wrongChar = decWord[index]
            rightChar = dicWord[index]
            if not (wrongChar in charList):
                charList[wrongChar] = dict()
                
            if not (rightChar in charList[wrongChar]):
                charList[wrongChar][rightChar] = 1
            else:  
                charList[wrongChar][rightChar] += 1
        
        index += 1
    
if __name__ == '__main__':
    matchCharacters()
    print charList
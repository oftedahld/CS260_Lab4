EMPTY = "_empty_"

class ChainLink:
    def __init__(self, value, nextLink=None):
        """Creates a single-pointed link with null pointers if not specified"""
        self.value = value
        self.next = nextLink

    def getValue(self):
        """Returns the value for the specified item"""
        return self.value

    def getNext(self):
        """Returns the location of the next link"""
        return self.next

    def setNext(self, next):
        """Sets the location of the next link"""
        self.next = next
    
    def clearNext(self):
        """Sets the location of the previous link"""
        self.next = None

class ChainHash:
    def __init__(self, arraySize = 7):
        """Creates a blank array of specified size"""
        if arraySize < 1:
            arraySize = 7
        self.arraySize = arraySize
        self.elementsCount = 0
        self.theArray = [EMPTY] * arraySize

    def hashFunc(self, key):
        # print(f"key: {key}") #TEMPORARY PRINT FOR TESTING, REMOVE FOR SUBMISSION
        hashValue = 0  #initialize index
        for i in range(0, len(key)):  #// walk through string one char at a time
            hashValue *= 128 #// multiply current sum
            hashValue += ord(key[i]) #// add current character's ascii value
            hashValue %= self.arraySize #// shrink to fit
        # print(f"hashValue: {hashValue}") #TEMPORARY PRINT FOR TESTING, REMOVE FOR SUBMISSION
        return hashValue #// return the result
    

    def addItem(self, value):
        """Adds value to the new table in the appropriate spot"""  
        if self.elementsCount + 1 > self.arraySize * 2:
            # print("Table Full")#TEMPORARY PRINT FOR TESTING, REMOVE FOR SUBMISSION
            self.resize()
        hashedIndex = self.hashFunc(value)
        tempLink = ChainLink(value)
        if self.theArray[hashedIndex] != EMPTY:
            tempLink.setNext(self.theArray[hashedIndex])
        self.theArray[hashedIndex] = tempLink
        self.elementsCount += 1
        
    def findItem(self, value):
        """return true if value is present in the table, false otherwise"""  
        hashedIndex = self.hashFunc(value)
        found = False
        link = self.theArray[hashedIndex]
        if link != EMPTY:
            while link != None and found == False:
                if link.getValue() == value:
                    found = True
                else:
                    link = link.getNext()
        return found

    def removeItem(self, value):
        """remove the item from the table if present, do nothing otherwise"""
        hashedIndex = self.hashFunc(value)
        link = self.theArray[hashedIndex]
        if link != EMPTY:
            if link.getValue() == value:
                if link.getNext() != None:
                    self.theArray[hashedIndex] = link.getNext()
                else:
                    self.theArray[hashedIndex] = EMPTY
            else:
                found = False    
                while link != None and found == False:
                    if link.getNext().getValue() == value:
                        link.setNext(link.getNext().getNext())
                        found = True
                    else:
                        link = link.getNext()

    def displayTable(self):
        """Returns a string with one line per element with its links separated by spaces. Empty cells should be shown as “_empty_”. There is example output in the Moodle document on separate chaining."""
        stringOutput = ""
        for i in range(0, self.arraySize):
            if self.theArray[i] != EMPTY: #If the array item is not empty, run through contents of the list
                link = self.theArray[i]
                while link != None:
                    stringOutput += str(link.getValue())
                    if link.getNext() != None:
                        stringOutput += " "
                    link = link.getNext()
            else: 
                stringOutput += self.theArray[i]
            if i != (self.arraySize - 1): #If current item is not the last one, add a newline afterwards
                stringOutput += "\n"
        return stringOutput
    
    def resize(self):
        """Resizes the table to the next prime number"""
        newSize = self.nextPrime((self.arraySize * 2) - 2) #starting number for prime search is double the current size minus 1
        oldSize = self.arraySize
        # print(f"New array size will be {newSize}") #TEMPORARY, REMOVE FOR FINAL SUBMIT
        tempList = self.theArray[:]
        self.theArray = [EMPTY] * newSize
        self.arraySize = newSize
        self.elementsCount = 0
        for i in range(0, oldSize):
            if tempList[i] != EMPTY:
                link = tempList[i]
                while link != None:
                    value = link.getValue()
                    self.addItem(value)
                    link = link.getNext()

    def isPrime(self, number):
        """Returns True if input number is prime, otherwise returns False"""
        for divisor in range (2, number):
            if number % divisor == 0:
                return False
        return True

    def nextPrime(self, value):
        """Returns the next  prime number"""
        size = value
        if size == 1:
            return 2
        primeCheck = size
        primeFound = False
        while(primeFound == False):
            primeCheck = primeCheck + 1
            if(self.isPrime(primeCheck) == True):
                primeFound = True
        return primeCheck
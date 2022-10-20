EMPTY = "_empty_"
DELETED = "_deleted_"    

class StringHash:    

    def __init__(self, arraySize = 11):
        """Creates a blank array of specified size"""
        if arraySize < 1:
            arraySize = 11
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
        if self.elementsCount >= self.arraySize/2:
            print("Table Full") #Need to add in actual resizing here
        else:
            hashedLocation = self.hashFunc(value)
        while self.theArray[hashedLocation] != EMPTY and self.theArray[hashedLocation] != DELETED:
            hashedLocation += 1
            if hashedLocation >= self.arraySize:
                hashedLocation = 0
        self.elementsCount += 1
        self.theArray[hashedLocation] = value
        print(f"{self.theArray[hashedLocation]} added at {hashedLocation}") #TEMPORARY PRINT FOR TESTING, REMOVE FOR SUBMISSION
    
    def findItem(self, value):
        """Return true if value is present in the table, false otherwise"""
        hashedLocation = self.hashFunc(value)
        itemsChecked = 1
        itemFound = False
        while itemsChecked <= self.elementsCount and itemFound == False:
            if self.theArray[hashedLocation] == value: #Check if the current hashed location contains the value
                itemFound = True
            else: #Increment hashedLocation or reset to 0 if end of array reached
                if self.theArray[hashedLocation] != EMPTY or self.theArray[hashedLocation] != DELETED: #If the value at the location was not empty or deleted, count towards total of elements checked
                    itemsChecked += 1
                if hashedLocation >= self.arraySize: 
                    hashedLocation = 0
                else:
                    hashedLocation += 0
        return itemFound

    def removeItem(self, value):
        """Remove the item from the table if present, do nothing otherwise"""
        hashedLocation = self.hashFunc(value)
        itemsChecked = 1
        itemFound = False
        while itemsChecked <= self.elementsCount and itemFound == False:
            if self.theArray[hashedLocation] == value: #Check if the current hashed location contains the value
                itemFound = True
            else: #Increment hashedLocation or reset to 0 if end of array reached
                if self.theArray[hashedLocation] != EMPTY or self.theArray[hashedLocation] != DELETED: #If the value at the location was not empty or deleted, count towards total of elements checked
                    itemsChecked += 1
                if hashedLocation >= self.arraySize: 
                    hashedLocation = 0
                else:
                    hashedLocation += 0
        if itemFound == True:
            print(f"Removing {self.theArray[hashedLocation]} from location {hashedLocation}") #TEMPORARY PRINT FOR TESTING, REMOVE FOR SUBMISSION
            self.theArray[hashedLocation] = DELETED
            self.elementsCount -= 1
            print(f"Location {hashedLocation} is now {self.theArray[hashedLocation]}") #TEMPORARY 
                

    def displayTable(self):
        """Returns a string with one line per element with its links separated by spaces."""

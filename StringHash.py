"""def hashFunc(key):
    hashValue = 0  #initialize index
    for i = 0; i < key.length(); i++ #// walk through string one char at a time
        hashValue *= 128 #// multiply current sum
        hashValue += key[i] #// add current character's ascii value
        hashValue %= arraySize #// shrink to fit
    return hashValue #// return the result
    """
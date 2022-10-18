from ChainedHash import ChainHash
from StringHash import StringHash

BASE_SIZE = 5
baseWords = "maple", "spruce", "oak", "cedar", "cherry"

ADV_SIZE = 10
advWords = "dog", "cat", "ape", "cow", "frog", "fish", "goat", "bear", "deer", "elk"

def main():
    #uncomment functions to run tests

    print("\nStringHash tests\n")

    # # Basic tests
    # testBaseFind()
    # testBaseRemove()
    # testBaseDisplay()
    # testBaseGrow()
    #
    # # Advanced tests
    # print("\nChainHash tests\n")
    #
    # testAdvFind()
    # testAdvRemove()
    # testAdvDisplay()
    #
    # #test thinking problem
    # testThink()


def testBaseFind():
    print("Testing addItem and findItem\n")
    baseFind = StringHash()

    for index in range(BASE_SIZE):
        baseFind.addItem(baseWords[index])
    
    print("Should find maple and not apple")
    if baseFind.findItem("maple"):
        print(" maple found")
    else:
        print(" maple not found")
    if baseFind.findItem("apple"):
        print(" apple found")
    else:
        print(" apple not found")

    print("\nDone testing addItem and findItem\n")

def testBaseRemove():
    print("Testing addItem, findItem, and removeItem\n")
    baseRemove = StringHash ()

    for index in range(BASE_SIZE):
        baseRemove.addItem(baseWords[index])
    
    print("Should find maple and then not find maple")
    if baseRemove.findItem("maple"):
        print(" maple found")
    else:
        print(" maple not found")
    baseRemove.removeItem("maple")
    if baseRemove.findItem("maple"):
        print(" maple found")
    else:
        print(" maple not found")
    print("Should find spruce")
    if baseRemove.findItem("spruce"):
        print(" spruce found")
    else:
        print(" spruce not found")
        
    print("\nDone testing addItem, findItem, and removeItem\n")

def testBaseDisplay():
    print("Testing addItem, findItem, removeItem, and display\n")
    baseList = StringHash()

    for index in range(BASE_SIZE):
        baseList.addItem(baseWords[index])
    
    baseList.removeItem("apple")
    print("Should be cedar cherry maple spruce 6(_empty_) oak")
    print(baseList.displayTable(), end = "")

    print("\nDone testing addItem, findItem, removeItem, and display\n")

def testBaseGrow():
    print("Testing growing StringHash\n")
    BASE_EXTRA = 3
    baseExtraWords = "bear", "pony", "cow"

    baseGrow = StringHash()

    for index in range(BASE_SIZE):
        baseGrow.addItem(baseWords[index])
    

    for index in range(BASE_EXTRA):    
        baseGrow.addItem(baseExtraWords[index])
    
    print("After growing the list should be ")
    print("_empty_ cherry _empty_ _empty_ _empty_ cow _empty_ _empty_ "
              + "_empty_ pony cedar _empty_ _empty_ maple spruce "
              + "_empty_ _empty_ _empty_ _empty_ _empty_ bear oak")
    print("The order might differ, but contents should not\n")
    print(baseGrow.displayTable())
    
    print("Now testing find and remove after growing")
    print("Should find maple and then not find maple")
    if baseGrow.findItem("maple"):
        print(" maple found")
    else:
        print(" maple not found")
        baseGrow.removeItem("maple")
    if baseGrow.findItem("maple"):
        print(" maple found")
    else:
        print(" maple not found")
    print("Should find spruce")
    if baseGrow.findItem("spruce"):
        print(" spruce found")
    else:
        print(" spruce not found")

    print("\nDone testing growing StringHash\n")

def testAdvFind():
    print("Testing addItem and findItem\n")
    advFind = ChainHash()

    for index in range(ADV_SIZE):
        advFind.addItem(advWords[index])

    if advFind.findItem("goat"):
        print(" goat was found")
    else:
        print(" goat was not found")
    if advFind.findItem("goat"):
        print(" horse was found")
    else:
        print(" horse was not found")

    print("\nDone testing addItem and findItem\n")

def testAdvRemove():
    print("Testing addItem, findItem, and removeItem\n")
    advRemove = ChainHash()

    for index in range(ADV_SIZE):
        advRemove.addItem(advWords[index])
    
    print("Should find goat and then not find goat")
    if advRemove.findItem("goat"):
        print(" goat was found")
    else:
        print(" goat was not found")

    advRemove.removeItem("goat")

    if advRemove.findItem("goat"):
        print(" goat was found")
    else:
        print(" goat was not found")

    print("\nDone testing addItem, findItem, and removeItem\n")

def testAdvDisplay():
    print("Testing addItem, findItem, removeItem, and display\n")
    advList = ChainHash()

    for index in range(ADV_SIZE):
        advList.addItem(advWords[index])

    advList.removeItem("goat")
    print("Should be: \n_empty_\ndeer frog\nfish cow\n"
                + "_empty_\ndog\nbear\nelk ape cat")
    print("The order might differ, but contents should not\n")
    print(advList.displayTable(), end = "")

    print("\nDone testing addItem, findItem, removeItem, and display\n")


def testThink():
    print("Testing thinking problem (growing ChainHash)\n")
    ADV_EXTRA = 6
    advExtraWords = "apple", "pine", "fir", "oak", "maple", "fig"

    advGrow = ChainHash()

    for index in range(ADV_SIZE):
        advGrow.addItem(advWords[index])
    
    for index in range(ADV_EXTRA):
        advGrow.addItem(advExtraWords[index])
    
    print("\nAfter growing the list should have 13 rows ")
    print("and include apple, pine, fir, oak, maple, fig, dog,")
    print("cat, ape, cow, frog, fish, goat, bear, deer, elk \n")
    print(advGrow.displayTable(), end = "")

    print("\nDone testing growing StringHash\n")


if __name__ == "__main__":
    main()

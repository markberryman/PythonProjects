class Hashtable(object):
    """Hashtable with open chaining for collision resolution."""

    def __init__(self, numSlots):
        self.numSlots = numSlots
        self.table = [[] for x in range(numSlots)]        

    def print(self):
        for list in self.table:
            print(str(list))

    def asciiSumHashFn(self, string):
        sum = 0

        for char in string:
            sum += ord(char)

        # bound value to range equal to num slots in the table
        return sum % self.numSlots

    def add(self, string):
        """Return bool indicating success of operation."""
        result = False

        hashValue = self.asciiSumHashFn(string)

        hashList = self.table[hashValue]

        if (string not in hashList):
            result = True
            hashList.append(string)

        return result

    def find(self, string):
        result = None

        hashValue = self.asciiSumHashFn(string)

        for item in self.table[hashValue]:
            if item == string:
                result = item
                break

        return result
        
    def remove(self, string):
        """Return bool indicating success of operation."""
        result = False

        hashValue = self.asciiSumHashFn(string)

        hashList = self.table[hashValue]

        if (string in hashList):
            result = True
            hashList.remove(string)
            
        return result

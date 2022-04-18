# KEY VALUE DATASTRUCTURE
# Handling collision using Chaining
class HashMap:
    def __init__(self, length) -> None:
        self.length = length
        self.table = [None for _ in range(self.length)]

    def getHash(self, key) -> int:
        sum = 0
        for character in key:
            sum += ord(character)
        
        return sum % self.length

    def addKeyValuePair(self, key, value) -> None:
        index = self.getHash(str(key))
        if self.table[index]:
            if type(self.table[index]) != list:
                temp = self.table[index]
                self.table[index] = []
                self.table[index].append(temp)
                self.table[index].append(value)
            else:
                self.table[index].append(value)
        else:
            self.table[index] = value

    def getValue(self, key) -> None:
        index = self.getHash(str(key))
        value = self.table[index]
        print(f"Value {value} is at the index {index}.")


    def displayHashMap(self) -> None:
        for i in range(self.length):
            if self.table[i] is not None:
                print(f"Key: {i}, Value: {self.table[i]}")

hm = HashMap(20)
hm.addKeyValuePair("Hanan", 22)
hm.addKeyValuePair("Asghar", 58)
hm.addKeyValuePair("asghar", 58)
hm.displayHashMap()
hm.getValue("asghar")
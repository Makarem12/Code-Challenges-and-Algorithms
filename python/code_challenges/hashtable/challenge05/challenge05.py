class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def custom_hash(self, key):
        return hash(key) % self.size

    def insert(self, key):
        index = self.custom_hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key)
        else:
            current = self.table[index]
            while current.next:
                if current.value == key:
                    return
                current = current.next
            if current.value != key:
                current.next = Node(key)

    def search(self, key):
        index = self.custom_hash(key)
        current = self.table[index]
        while current:
            if current.value == key:
                return True
            current = current.next
        return False

def intersection(arr1, arr2):
    ht1 = HashTable()
    ht2 = HashTable()
    result = []

    for num in arr1:
        ht1.insert(num)

    for num in arr2:
        if ht1.search(num) and not ht2.search(num):
            result.append(num)
            ht2.insert(num)

    return result



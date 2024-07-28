class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def custom_hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.custom_hash(key)
        if not self.table[index]:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        index = self.custom_hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

def reorder_people_by_height(names, heights):
    # Create a hashtable and store people with heights
    hashtable = HashTable()
    for i in range(len(names)):
        hashtable.insert(heights[i], names[i])

    # Sort heights in descending order
    sorted_heights = sorted(heights, reverse=True)

    # Retrieve names in the order of sorted heights
    sorted_names = []
    for height in sorted_heights:
        sorted_names.append(hashtable.get(height))
    
    return sorted_names




import hashlib
# '''
# Linked List hash table key/value pair
# '''

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return int(hashlib.sha256(b"key").hexdigest(), 16)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        node = LinkedPair(key, value)
        index = self._hash_mod(key)

        # if self.storage[index] is None:
        #     self.storage[index] = node
        # else:
        node.next = self.storage[index]
        self.storage[index] = node

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            print(f"{key} does not exist in table")
            return
        else:
            if self.storage[index].key == key:  # first one is node to delete
                print("hello")
                del_node = self.storage[index]
                # change index to start at next node (removing reference to first node)
                self.storage[index] = self.storage[index].next
                return del_node  # return deleted node
            else:
                print("i'm in else")
                current_node = self.storage[index]
                prev_node = self.storage[index]
                while current_node:  # goes through whole linked list
                    if current_node.key == key:
                        prev_node.next = current_node.next
                        return current_node  # return deleted node
                    else:
                        prev_node = current_node
                        current_node = current_node.next
                # if doesn't return then not in linked list...so after loop, return warning?
                print(f"{key} does not exist in table")
                return

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_node = self.storage[index]

        while current_node:
            if current_node.key == key:
                return current_node.value
            else:
                current_node = current_node.next

        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_ht = HashTable(self.capacity) #create temporary hashtable to create new storage
        
        for pair in self.storage:
            while pair:
                new_ht.insert(pair.key, pair.value)
                pair = pair.next #move on to the next node while exists
        
        self.storage = new_ht.storage #set storage of original ht to the new storage
            

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

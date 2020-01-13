class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0 #count is how much is currently used
        self.capacity = capacity #how much is currently allocated
        self.storage = [None] * self.capacity
    
    def insert(self, index, value):
        if self.count == self.capacity:
            self.resize()
            return
    
        #shift everything to the right
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]
        
        #insert our value
        self.storage[index] = value
        self.count += 1
    
    def append(self, value):
        self.insert(self.count, value)

    def resize(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage
    
    def replace(self, index, value):
        self.storage[index] = value

    def add_to_front(self, value):
        self.insert(0, value)

    def slice(self, start_index, end_index): #default value
        #beginning and end
        #subarray to store values

        #copy beginning to end to subarray

        #what happens to the original array?

        #return subarray

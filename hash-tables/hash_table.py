class HashTable:
    # constructor
    def __init__(self, size = 7):
        self.data_map = [None] * size

    # hash function
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    # prints entire Hash Table
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    # calculates and stores key-value pair at calculated address
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    # retrieves value based on specified key
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
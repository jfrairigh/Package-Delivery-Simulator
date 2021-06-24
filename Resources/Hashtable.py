class Hashtable:
    # time complexity: O(n)
    # space complexity: O(n)
    def __init__(self, initial_capacity=80):  # building the skeleton of the table
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])  # using a list in case two items have the same hash value (chaining)

    # time complexity: O(n)
    # space complexity: O(n)
    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for mapping in bucket_list:  # iterate through bucket_list's list of key/value pairs
            if mapping[0] == key:  # if key already exists update the value
                mapping[1] = value

        key_value = (key, value)  # if key does not exist add new key value pair
        bucket_list.append(key_value)

    # time complexity: O(n)
    # space complexity: O(n)
    def look_up(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for mapping in bucket_list:
            if mapping[0] == key:
                return mapping[1]
        return None

    # time complexity: O(n)
    # space complexity: O(n)
    def all_keys(self):
        all_keys = []
        for i in range(len(self.table)):  # iterate through list of bucket_lists
            for mapping in self.table[i]:  # iterate through list of key/value pairs
                all_keys.append(mapping[0])
        return all_keys

    # time complexity: O(n)
    # space complexity: O(n)
    def print_all(self):
        for i in range(len(self.table)):  # iterate through list of bucket_lists
            for mapping in self.table[i]:  # iterate through list of key/value pairs
                print(mapping[1])

    # time complexity: O(n)
    # space complexity: O(n)
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for mapping in bucket_list:
            if mapping[0] == key:
                bucket_list.remove([mapping[0], mapping[1]])

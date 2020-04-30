# For the first step, time taken depends on the K and the hash function.
# For example, if the key is a string “abcd”, then it’s hash function may depend on the length of the string. But for very large values of n, the number of entries into the map, length of the keys is almost negligible in comparison to n so hash computation can be considered to take place in constant time, i.e, O(1).
# For the second step, traversal of the list of K-V pairs present at that index needs to be done. For this, the worst case may be that all the n entries are at the same index. So, time complexity would be O(n). But, enough research has been done to make hash functions uniformly distribute the keys in the array so this almost never happens.
# So, on an average, if there are n entries and b is the size of the array there would be n/b entries on each index. This value n/b is called the load factor that represents the load that is there on our map.
# This Load Factor needs to be kept low, so that number of entries at one index is less and so is the complexity almost constant, i.e., O(1).

# Rehashing is done because whenever key value pairs are inserted into the map, the load factor increases, which implies that the time complexity also increases as explained above. This might not give the required time complexity of O(1).
# Hence, rehash must be done, increasing the size of the bucketArray so as to reduce the load factor and the time complexity.

class LinkedListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    
    def __init__(self, initial_size = 10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        
    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        # Head refers to the end of the linked list
        # Why do we need the head refeerence again? Because in the previous key check, we have made our head to become None

        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1
        
    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        print('heads value is ', head.value)
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
        
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                       # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   # compress coefficient

        return hash_code % num_buckets                                # one last compression before returning
    
    def size(self):
        return self.num_entries


    #When our load factor goes beyond 0.7, we need to rehash the function to achieve a O(1) lookup time.
    #We multiply the old number of entries by 2
    #We change the old array to become a new initialized array of all Nones
    #We keep a reference of the old array
    #Then we loop through each element, then traverse through that element's Linked List
    def rehash(self):
        old_num_entries = self.num_entries
        old_bucket_array = self.bucket_array
        new_num_entries = 2 * old_num_entries
        self.bucket_array = [None for _ in range(new_num_entries)]

        #array forward traversal
        for head in old_bucket_array:
            #linkedlist traversal
            while head is not None:
                key = head.key
                value = head.value
                self.put(key, value)
                head = head.next

    def delete(self, key):
        bucket_index = self.get_bucket_index(key)
        previous = None
        head = self.bucket_array[bucket_index]

        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                
                self.num_entries -= 1
                return
            else:
                previous = head
                head = head.next






hash_map = HashMap()

hash_map.put("one", 1)
hash_map.put("one", 12)
hash_map.put("one", 123)
hash_map.put("two", 2)
hash_map.put("three", 3)

print("size: {}".format(hash_map.size()))


print("one: {}".format(hash_map.get("one")))
# print("neo: {}".format(hash_map.get("neo")))
# print("three: {}".format(hash_map.get("three")))
# print("two: {}".format(hash_map.get("two")))
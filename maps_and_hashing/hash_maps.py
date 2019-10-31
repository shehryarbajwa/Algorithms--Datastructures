class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:

    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 37
        self.num_elements = 0

    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key , value)
        head = self.bucket_array[bucket_index]

        #check if key is already present in the map, and update it's value
        #Check if the head is not none
        while head is not None:
            #If the head's key is the same as the key we are trying to put
            #Then its value will be the value we are trying to put
            
            if head.key == key:
                head.value = value
                return
            #If the head.key != key, we can move on to the next head
            #
            head = head.next

        #If head is None, then we get the head node
        #New_node.next becomes head
        #
        head = self.bucket_array[bucket_index]
        
        self.bucket_array[bucket_index] = new_node
        self.num_elements += 1

    
    def get(self, key):
        bucket_index = self.compressed_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
    
    def size(self):
        return self.num_elements

    #Bucket index refers to the index at which we are going to store the value of the key element
    #abc will be stored at 3
    def get_bucket_index(self, key):
        return self.compressed_hash_code(key)

    # def get_hash_code(self, key):
    #     key = str(key)
    #     num_buckets = len(self.bucket_array)
    #     current_coefficient = 1
    #     hash_code = 0

    #     for character in key:
    #         hash_code += ord(character) * current_coefficient
    #         current_coefficient = current_coefficient * self.p
    #         current_coefficient = current_coefficient
        
    #     return hash_code

    def compressed_hash_code(self,key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0

        for character in key:
            hash_code += ord(character) * current_coefficient
            current_coefficient = current_coefficient * self.p
            current_coefficient = current_coefficient % num_buckets
        
        return hash_code % num_buckets




def hash_function(string):
    hash_code = 0

    for character in string:
        hash_code += ord(character)
    return hash_code


print(hash_function('abcd'))

hash_map = HashMap()
bucket_indexs = hash_map.compressed_hash_code('abcdeft')
bucket_indexes = hash_map.compressed_hash_code('abcdefg')
bucket_indexes1 = hash_map.compressed_hash_code('abcdefgi')
print(bucket_indexs)
print(bucket_indexes)
print(bucket_indexes1)

hash_map = HashMap()

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)
hash_map.put("one.", 1)
hash_map.put("one..", 1)

print("size: {}".format(hash_map.size()))


print("one: {}".format(hash_map.get("one")))
print("one.: {}".format(hash_map.get("one.")))
print("one..: {}".format(hash_map.get("one..")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("size: {}".format(hash_map.size()))

# For starters, it will return the same value for abcd and bcda. 
# Do we want that? We can create 24 different permutations for the string abcd and each will have the same value. 
# We cannot put 24 values to one index.

# When two different inputs produce the same output, then we have something called a collision. 
# An ideal hash function must be immune from producing collisions.

# For a string, say abcde, a very effective function is treating this as number of prime number base p. Let's elaborate this statement.

# For a number, say 578, we can represent this number in base 10 number system as
# 5∗102+7∗101+8∗100
 
# Similarly, we can treat abcde as
# 𝑎∗𝑝4+𝑏∗𝑝3+𝑐∗𝑝2+𝑑∗𝑝1+𝑒∗𝑝0
 
# Here, we replace each character with its corresponding ASCII value.
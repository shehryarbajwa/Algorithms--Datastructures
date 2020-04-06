#Design a hash map without using the built in hash-table libraries

# Design a put method put(key,value) - Insert a key/value pair into the hash map
# get(key) Returns the value to which the specified key is mapped or -1 if this key is not found
# remove(key) Removes the mapping for the value key 

# We can use ord('abcd') but it will be the same as ord('bcda')
# Our hashing function should be able to handle collisions 
# Once we have a hashing function that hashes strings to a list index, we can append to array and return the value in constant time

#The hash function for integers will be different from the hash function for strings, which again, will be different for some object of a class that you created.


class Hashmap:

    def __init__(self, initial_size = 10):
        self.array = [None for _ in range(initial_size)]
        self.prime = 37
    
    def put(self, key, value):
        hash_key = self.generate_hash(key)
        new_node = [key, value]

        if self.array[hash_key] is None:
            self.array[hash_key] = list([new_node])
        else:
            for pair in self.array[hash_key]:
                if pair[0] == key:
                    pair[1] = value
            self.array[hash_key].append(new_node)

    def get(self, key):
        hash_key = self.generate_hash(key)

        if self.array[hash_key] is not None:
            for pair in self.array[hash_key]:
                if pair[0] == key:
                    return pair[1]
        else:
            return None

    def delete(self, key):
        hash_key = self.generate_hash(key)

        if self.array[hash_key] is None:
            return None
        else:
            for i in range(0, len(self.array[hash_key])):
                if self.array[hash_key][i][0] == key:
                    self.array[hash_key].pop(i)
        
        return self

    def print(self, key):
        hash_key = self.generate_hash(key)

        if self.array[hash_key] is not None:
            for pair in self.array[hash_key]:
                return pair
        else:
            return False

    def generate_hash(self, key):
        hash_code = 0
        current_coefficient = 1
        array_length_for_compression = len(self.array)

        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % array_length_for_compression
            current_coefficient *= self.prime
            current_coefficient = current_coefficient % array_length_for_compression
        
        return hash_code

            
    
hash_map = Hashmap()
hash_map.put('Beans',3.25)
hash_map.put('Rice',3.05)
hash_map.put('Bananas',1.93)
hash_map.put('Oranges',1.98)
hash_map.put('Guava',2.36)

print(hash_map.print('kjndsfkjsdnfk'))
print(hash_map.print('banas'))
print(hash_map.print('Bananas'))

class HashMap:

    def __init__(self):
        self.num_elements = 0

    def put(self, key, value):
        pass
    
    def get(self, key):
        pass
    
    def size(self):
        return self.num_elements


def hash_function(string):
    hash_code = 0

    for character in string:
        hash_code += ord(character)
    return hash_code


print(hash_function('abcd'))

# For starters, it will return the same value for abcd and bcda. 
# Do we want that? We can create 24 different permutations for the string abcd and each will have the same value. 
# We cannot put 24 values to one index.

# When two different inputs produce the same output, then we have something called a collision. 
# An ideal hash function must be immune from producing collisions.


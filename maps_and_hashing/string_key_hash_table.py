#Write your own hash table and hash function that uses string keys
#Your table will store strings in buckets by their first two letters, according to the formula below

#Hash Value = (ASCII Value of First Letter * 100) + (ASCII Value of Second Letter)
#You can assume that the string will have atleast two letters, and the first two letters are uppercase letters
#ord() to get the ASCII value of a letter
#chr() to get the letter associated with an ASCII value

#Question is how large do you want the hash table to be ?
#Since UDACITY will be 8568, it is safe to assume that we can make our hash table to be of size 10,000




class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        # ""Return the hash value if the string is already in the table. Return -1 otherwise""
       
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    return hv
        return -1
    #If the string is long enough, its hash code will be bigger than the largest integer we can store on 32bits CPU
    #In that case, the hash code can be negative
    #It wont be in our helper function, but if we take ASCII for each string character, it might
    #Therefore we should always on the safe side, include -1 if 
    def calculate_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        print("hashCode for inputString is {}".format(value))
        return value

# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print (hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print (hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print (hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print (hash_table.lookup('UDACIOUS'))
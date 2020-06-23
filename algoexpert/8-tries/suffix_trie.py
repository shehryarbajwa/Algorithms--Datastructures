#Time Complexity O(N^2)
#Space Complexity O(N^2)


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = '*'
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insert_substring_starting_at(i, string)

    def insert_substring_starting_at(self,i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True
    
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node  
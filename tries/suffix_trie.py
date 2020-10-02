class Trie:
    def __init__(self, string):
        self.root = {}
        self.end_symbol = '*'
        self.populate_trie(string)

    def populate_trie(self, string):
        for i in range(len(string)):
            self.build_tree(i, string)

    #Creation is O(N^2) since N^2 is using double for loops for finding suffixes for each string
    #Space Complexity is O(N^2) since we are storing each suffix for each word
    def build_tree(self, index, string):
        current = self.root
        for i in range(index, len(string)):
            letter = string[i]
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    #Search is O(M) time complexity
    #Search is O(1) space complexity
    def contains(self, string):
        current = self.root
        for letter in string:
            if letter not in current:
                return False
            current = current[letter]
        return self.end_symbol in current

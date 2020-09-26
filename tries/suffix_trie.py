class Trie:
    def __init__(self, string):
        self.root = {}
        self.end_symbol = '*'
        self.populate_trie(string)

    def populate_trie(self, string):
        for i in range(len(string)):
            self.build_trie(i, string)

    def build_trie(self, index, string):
        root = self.root
        for i in range(index, len(string)):
            letter = string[i]
            if letter not in root:
                root[letter] = {}
            root = root[letter]
        root[self.end_symbol] = True

    def contains(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return True

class Trie:
    def __init__(self, string):
        self.root = {}
        self.end_symbol = '*'
        self.populate_trie(string)

    def populate_trie(self, string):
        for i in range(len(string)):
            self.build_tree(i, string)

    def build_tree(self, index, string):
        current = self.root
        for i in range(index, len(string)):
            letter = string[i]
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def contains(self, string):
        current = self.root
        for letter in string:
            if letter not in current:
                return False
            current = current[letter]
        return self.end_symbol in current

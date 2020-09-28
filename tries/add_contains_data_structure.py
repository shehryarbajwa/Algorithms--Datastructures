class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def add_word(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def contains(self, string):
        current = self.root

        def helper(word, node):
            for idx, letter in enumerate(word):
                if letter not in node:
                    if letter == '.':
                        for char in node:
                            if char != self.end_symbol and helper(word[idx + 1:], node[char]):
                                return True
                    return False
                else:
                    current = current[letter]
        
        return helper(string, current)

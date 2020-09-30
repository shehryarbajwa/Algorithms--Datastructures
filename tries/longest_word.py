def longest_word(words):
    trie = Trie()
    for word in words:
        trie.add_word(word)
    return trie.return_max_word()

class Trie(object):
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'


    def add_word(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = word

    def return_max_word(self):
        stack = self.root.values()
        ans = ''
        while stack:
            current = stack.pop()
            if '*' in current:
                #Find current word associated with end symbol
                word = current[self.end_symbol]
                #If existing word is greater than ans
                #If existing word comes alphabetically before the ans
                #Update ans
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                for letter in current:
                    if letter != self.end_symbol:
                        stack.append(current[letter])
            else:
                continue
        return ans


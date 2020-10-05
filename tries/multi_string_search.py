
def multi_string_search(big_string, small_strings):
    visited = [False for entry in small_strings]
    trie = Trie()
    for word in small_strings:
        trie.add_word(word)
    contained_strings = {}
    for i in range(len(big_string)):
        find_small_strings(i, big_string, contained_strings, trie)
    
    for index, word in enumerate(small_strings):
        if word in contained_strings:
            visited[index] = True
        else:
            visited[index] = False
    return visited


def find_small_strings(index, big_string, contained_strings, trie):
    current = trie.root
    for i in range(index, len(big_string)):
        current_char = big_string[i]
        if current_char not in current:
            break
        current = current[current_char]

        if trie.end_symbol in current:
            contained_strings[current[trie.end_symbol]] = True




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

    
print(multi_string_search('this is a big string', ["this", "yo", "is", "a", "bigger", "string", "kappa"]))
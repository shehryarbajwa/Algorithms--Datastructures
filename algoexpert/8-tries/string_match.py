
#Time Complexity O(ns + bs)
#Space Complexity O(ns)

def multi_string_search(big_string, small_string):
    trie = Trie()
    for string in small_string:
        trie.insert(string)
    contained_strings = {}
    for i in range(len(big_string)):
        find_small_strings_in(big_string, i, trie, contained_strings, )
    return [string in contained_strings for string in small_string]

def find_small_strings_in(big_string, start_idx, trie, contained_strings):
    current_node = trie.root
    for i in range(start_idx, len(big_string)):
        current_char = string[i]
        if current_char not in current_node:
            break
        current_node = current_node[current_char]
        if trie.end_symbol in current_node:
            contained_strings[current_node[trie.end_symbol]] = True

class Trie:
    def __init__(self, string):
        self.root = {}
        self.end_symbol = '*'

    def insert(self, string):
        node = self.root
        for i in range(len(string)):
            letter = string[i]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.end_symbol] = string
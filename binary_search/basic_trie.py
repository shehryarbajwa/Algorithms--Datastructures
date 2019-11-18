#In this 
basic_trie = {
    'c' : {
        'e': {
            'o': {'word_end': True},
            'word_end': False}
        },
    'h': {
        'e':{
            'l':{
                'l': {
                    'o': {'word_end': True},
                          'word_end': False
                } 
            }
        },
        'a': {
            'l': {
                'f': {'word_end': True},
                'word_end': False
            }
        },
        'i': {'word_end': True},
                'word_end': False
    }
}


#Above is a normal trie with the words hi added in it
#We need to define a function where we can calculate whether that word exists in the trie
#

def is_word(word):
    current_node = basic_trie

    for char in word:
        if char not in current_node:
            return False
        
        current_node = current_node[char]
    return current_node['word_end']

print(is_word('hi'))

#Trie Using a Class
#Implement a trie to add a word to the Trie
#Implement exists to return True if the word exist in the trie and False if the word doesn't exist in the trie.

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word = True

    def exists(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word

#In add, we are doing the same thing, we are looping over each element in the word
#If that word exists we increment the current node by the character
#If it doesnt exist in the current_node.children which is a dictionary, then we upend the
#current_node.children[h] = TrieNode() so that now we can create its childrens. i.e h's childrens
#For the second char in word which is i
#if char not in current_node.children which is True
#current_node is now current_node.children[h] becomes current_node.children[h].children[i] = TrieNode()
#Now we finish our loop for char in word
#Therefore we return current_node.children[h].children[i].is_word = True
#Thats it we have added hi to our trie

#Now for example we have the word hello
#We know that h exists
#If we are adding, then we know that h exists in the dictionary so we move on setting current_node = current_node.children['h'
#Now we are on e
#if char not in current_node.children[h].children
#Which is true
#So then we add current_node.children[h].children[e]
#This way we keep one char for key and then can have as many children for its childrens
#Thus each character can be represented once by the hash hash[a] hash[b] hash[c] and ...
#And each of those hashes can have as many children as they want creating a tree like structure

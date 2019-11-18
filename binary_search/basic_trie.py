#In this 
basic_trie = {
    'c' : {
        'e': {
            'o': {'word_end': True},
            'word_end': False}
        },
'h': {
        'i': {  'word_end': True},
        'word_end': False}
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

print(is_word('ceo'))
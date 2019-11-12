import sys

class HuffNode(object):

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def is_leaf(self):
        return not (self.left or self.right)

#Data is the string
#For example EXAMPLE
#In the frequency map, we store the number of times each element is repeated
#If it is not in frequency_map, we add 1 to it
#If it is, then we increment it by 1

#Then we create the frequencies array
#We will loop through each key, value pair in dictionary and append to our frequencies our HuffNode
#The huffnode will have the values of char and frequencies
#HuffNode(E,2)
#HuffNode(X,1)
#HuffNode(A,1)
#HuffNode(M,1)
#HuffNode(P,1)
#HuffNode(L,1)
#Now our frequencies array has 6 entries at each index there exists a HuffNode


def create_frequency_list(data):
    frequency_map = {}

    for char in data:
        if char not in frequency_map.keys():
            frequency_map[char] = 1
        else:
            frequency_map[char] += 1
    
    frequencies = []

    for char, freq in frequency_map.items():
        frequencies.append(HuffNode(char, freq))
    return frequencies

#Then we will sort our frequencies array with the highest frequencies first and lowest on the bottom
#That way when we construct our HuffTree, we can find the lowest elements
#x.freq will look at each frequency and arrange from A-1 to E-2
#Then we use reverse=True to reverse that order so now E-2 is first and A-1 is last
def sort_frequencies(frequencies):
    sorted_frequencies = sorted(frequencies, key=lambda x:x.freq, reverse=True)
    return sorted_frequencies

def build_huff_tree(text):
    #We will first create the frequencies from the text provided in array form
    #Then we will sort that array based on top items with most frequencies and bottom with least

    frequencies = create_frequency_list(text)
    frequencies = sort_frequencies(frequencies)

    while len(frequencies) > 1:
        #At left and right we will pop out two smallest Nodes
        left = frequencies.pop()
        right = frequencies.pop()
        #Then we will calculate the sum of the frequencies
        freq_sum = left.freq + right.freq
        #Parent node has no character just the frequency sum
        parent = HuffNode(None, freq_sum)
        #Then we assign the parent node pointers to left and right
        parent.left = left
        parent.right = right

        #update frequency list
        #So since it is a while loop, we will keep popping the values from left and right
        #Until we have append only the parent node which wont have char just the parent element

        #So in our case in the first while loop, p and l go out of the frequency list
        #{'E': 2, 'X': 1, 'A': 1, 'M': 1, 'P': 1, 'L': 1}
        #And We append Parent which is (None,2) at the end of the list
        #And then we also sort the frequencies again.
        #Then once again, we take out A,M
        #Once A,M is taken out, we will append their parent node
        #Then we will take out E and X
        #Again append their parent node
        #In the end we will have our frequencies to just return Parent Nodes
        frequencies.append(parent)
        frequencies = sort_frequencies(frequencies)
    #Return frequencies[0] as the parent node
    return frequencies[0]

#In our case now, EXAMPLE has 5 Nones which have no char just frequency and 6 characters which donot have a right or left node
#So in our trim_huff_tree code, we go down multiple steps to reach the leaf of the tree
#When we reach the tree leaf, we add that char as key in the hash_map dict and the code as its value
#Each time we traverse left, we add 0
#Each time we traverse right,we add 1
#We start with the parent node
#Remember when we build our huff_tree, we build the entire tree and return the parent node by frequencies[0]
#So from the parent node, we do recursion to traverse each side
#When there is no longer a tree and all leafs have been checked, we return huff_map
def trim_huff_tree(tree, code):
    huff_map = {}
    if not tree:
        return huff_map
    if tree.is_leaf():
        huff_map[tree.char] = code
    huff_map.update(trim_huff_tree(tree.left, code + '0'))
    huff_map.update(trim_huff_tree(tree.right, code + '1'))
    return huff_map

#In decode_next, we receive the the data form huffman decoding which is a string of 110001101010110011
#Index provided is 0
#We start from tree which is the result of huffman_coding which is the parent node
#Data is 1100101
#data[0] = 1
#Tree is parent node
#If the tree is leaf, then return tree.character and the index
#If the data[index] == 0, then we increment index by 1 and look to the tree's left
#If the data[index] == 1, then we incremennt index by 


def decode_next(data, index, tree):
    assert(tree)
    assert(len(data) > 0)
    if tree.is_leaf():
        return tree.char, index
    if data[index] == '0':
        return decode_next(data, index + 1, tree.left)
    else:
        return decode_next(data, index + 1, tree.right)


def huffman_encoding(text):
    huff_tree = build_huff_tree(text)
    huff_map = trim_huff_tree(huff_tree, '')
    data = ''
    #Once we have our huff_map, we can then take all the values of each element
    #and return it in one long string
    #Like 011010101 to return e.g abcd
    #
    for char in text:
        data += huff_map[char]
    return data, huff_tree

def huffman_decoding(data, tree):
    #next_index returns the string E,X,A,M,P,L,E
    #while next_index < len(data) which is true since next_index has length of 
    #Data here is encoded text 0010021100210
    #We start at 0
    #Tree is parent node
    #Tree is in node form
    #
    text, next_index = decode_next( data, 0, tree )
    print('len of next index is ' + next_index)
    while next_index < len(data):
        next_char, next_index = decode_next( data, next_index, tree )
        text += next_char
    return text
import sys

class HuffNode(object):
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def is_leaf(self):
        return not (self.left or self.right)


def create_frequency_list(data):
    frequency_map = {}
    for char in data:
        if char not in frequency_map.keys():
            frequency_map[char] = 1
        else:
            frequency_map[char] += 1
    frequencies = []
    for char, freq in frequency_map.items():
        frequencies.append( HuffNode(char, freq) )
    
    return frequencies


def sort_frequencies(frequencies):
    sorted_frequencies = sorted(frequencies, key=lambda x: x.freq, reverse=True)
    return sorted_frequencies


def build_huff_tree(text):
    frequencies = create_frequency_list( text )
    frequencies = sort_frequencies( frequencies )
    while len(frequencies) > 1:
        # take out two smallest nodes
        left = frequencies.pop()
        right = frequencies.pop()
        freq_sum = left.freq + right.freq
        # create new parent sum node
        parent = HuffNode( None, freq_sum )
        parent.left = left
        parent.right = right
        # update frequency list

        frequencies.append( parent )
        frequencies = sort_frequencies( frequencies )
   
    return frequencies[0]

#
def envision_code_huff_tree(tree, code):
    huff_map = {}
    if not tree:
        return huff_map
    if tree.is_leaf():
        huff_map[tree.char] = code
    
    huff_map.update( envision_code_huff_tree( tree.left, code + '0' ) )
    huff_map.update( envision_code_huff_tree( tree.right, code + '1' ) )
   
    return huff_map

#In decode_next, we receive the data form huffman decoding which is a string of 110001101010110011
#Index provided is 0
#Data[0] == 1
#We start from tree which is the result of huffman_coding which returns huff_tree which is frequencies[0] which is the parent node
#If the tree is the leaf, we return the tree.char. Tree right now is a Node which at beginning is the parent Node
#If it is one, we recurse to the right side of the tree
#WHen we reach if tree.is_leaf()
#Then we return the tree.char
def decode_next(data, index, tree):
    assert(tree)
    assert(len(data) > 0)
    if tree.is_leaf():
        print(tree.char)
        return tree.char, index
    if data[index] == '0':
        return decode_next( data, index + 1, tree.left )
    else:
        return decode_next( data, index + 1, tree.right )


def huffman_encoding(text):
    assert(text)
    huff_tree = build_huff_tree( text )
    huff_map = envision_code_huff_tree( huff_tree, '' )
    data = ''
    for char in text:
        data += huff_map[char]
        print('data is ' + data)
    print('huff tree is ' + str(huff_tree))
    return data, huff_tree


def huffman_decoding(data, tree):
    assert(data)
    assert(tree)
    text, next_index = decode_next( data, 0, tree )
    #next_index returns the 
    print('len of next index is ' + str(next_index))
    
    while next_index < len(data):
        next_char, next_index = decode_next( data, next_index, tree )
        text += next_char
    return text

def test_encoding(text):
    print ("Original Text:\t\t {}".format( text ))
    print ("Size:\t\t\t {}".format( sys.getsizeof(text) ))
    
    encoded_data, tree = huffman_encoding(text)
    print ("Huffman Encoding:\t {}".format(encoded_data))
    print ("Size:\t\t\t {}".format( sys.getsizeof( int(encoded_data, base=2) )))
    
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("Decoded Text:\t\t {}".format(decoded_data))
    print ("Size:\t\t\t {}".format( sys.getsizeof(decoded_data) ))
    
    return decoded_data == text

print( test_encoding("EXAMPLE") )
#Original Text:     ABBBBABBABABBBAABABABAABABA
#Size:              76
#Huffman Encoding:  011110110101110010101001010
#Size:              28
#Decoded Text:      ABBBBABBABABBBAABABABAABABA
#Size:              76
#True

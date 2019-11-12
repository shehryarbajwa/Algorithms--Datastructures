import sys

class HuffNode(object):
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def is_tree_leaf(self):
        if (self.left or self.right) is None:
            return True
        else:
            return False


def element_frequency_list(data):
    frequency_dict = {}
    for element in data:
        if element not in frequency_dict:
            frequency_dict[element] = 1
        else:
            frequency_dict[element] += 1
    node_frequencies = []

    for key, value in frequency_dict.items():
        node_frequencies.append(HuffNode(key, value))
    return node_frequencies

def sort_node_frequencies(node_frequencies):
    sorted_frequencies = sorted(node_frequencies, key=lambda x:x.freq, reverse=True)
    return sorted_frequencies

def build_huff_tree(text):
    frequencies = element_frequency_list(text)
    frequencies_sorted = sort_node_frequencies(frequencies)

    while len(frequencies_sorted) > 1:
        left = frequencies_sorted.pop()
        right = frequencies_sorted.pop()

        freq_count = left.freq + right.freq

        parent = HuffNode(None, freq_count)
        parent.left = left
        parent.right = right
        frequencies_sorted.append(parent)
        frequencies_sorted = sort_node_frequencies(frequencies_sorted)
    
    return frequencies_sorted[0]

def assign_code_huff_tree(tree, code):
    huff_map = {}
    if not tree:
        return huff_map
    if tree.is_tree_leaf():
        huff_map[tree.char] = code
    huff_map.update(assign_code_huff_tree(tree.left, code + '0' ))
    huff_map.update(assign_code_huff_tree(tree.right, code + '1'))
    return huff_map

def decode_next_element(data, index, tree):
    if tree.is_tree_leaf():
        return tree.char, index
    if data[index] == '0':
        return decode_next_element(data, index + 1, tree.left)
    else:
        return decode_next_element(data, index + 1, tree.right)

def encode_tree(text):
    huff_tree = build_huff_tree(text)
    huff_map = assign_code_huff_tree(huff_tree, '')
    data = ''

    for char in huff_map:
        data += huff_map[char]
    return data, huff_tree

def decode_tree(data, tree):
    text, next_index = decode_next_element(data, 0, tree)

    while next_index < len(data):
        next_element, next_index = decode_next_element(data, next_index, tree)
        text += next_element
    return text

def test_encoding(text):
    print ("Original Text:\t\t {}".format( text ))
    print ("Size:\t\t\t {}".format( sys.getsizeof(text) ))
    
    encoded_data, tree = encode_tree(text)
    print ("Huffman Encoding:\t {}".format(encoded_data))
    print ("Size:\t\t\t {}".format( sys.getsizeof( int(encoded_data, base=2) )))
    
    decoded_data = decode_tree(encoded_data, tree)
    print ("Decoded Text:\t\t {}".format(decoded_data))
    print ("Size:\t\t\t {}".format( sys.getsizeof(decoded_data) ))


####Test Cases
#Test case 1
print( test_encoding("ABBBBABBABABBBAABABABAABABA") )

#Test case 2
print( test_encoding("EXAMPLE") )

#Test case 3
print( test_encoding("BABAAABBAEIOULMNOP") )

        
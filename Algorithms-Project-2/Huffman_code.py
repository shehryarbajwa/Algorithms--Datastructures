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
        frequencies.append(HuffNode(char, freq))
    return frequencies

def sort_frequencies(frequencies):
    sorted_frequencies = sorted(frequencies, key=lambda x:x.freq, reverse=True)
    return sorted_frequencies


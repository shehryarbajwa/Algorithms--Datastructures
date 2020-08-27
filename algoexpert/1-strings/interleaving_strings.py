
#a -> 'hacker'
#b -> 'good'
#res -> 'hgaocokder'

import unittest

def interleave(a, b):
    i, j = 0 , 0
    new_str = ""

    while i < len(a) and j < len(b):
        new_str += a[i] + b[j]

        i += 1
        j += 1

    while i < len(a):
        new_str += a[i]
        i += 1
    
    while j < len(b):
        new_str += b[j]
        j += 1

    return new_str

class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(interleave('hacker', 'good'), 'hgaocokder')

if __name__ == '__main__':
    unittest.main()



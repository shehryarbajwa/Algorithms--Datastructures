import unittest

## Time Complexity O(N)
## Space Complexity O(1)

def countManipulations(s1, s2):  

    if len(s1) is not len(s2):
        return -1
      
    count = 0
    count_2 = 0
    array = [0] * 26
      
    for i in range(len(s1)):  
        array[ord(s1[i]) - ord('a')] += 1

    for i in range(len(s2)):  
        array[ord(s2[i]) - ord('a')] -= 1

    for i in range(len(array)):
        if array[i] > 0:
            count += array[i]
        else:
            count_2 += abs(array[i])
            
    return [count, count_2]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(countManipulations('todo', 'toso'), [1,1])

    def test_case_2(self):
        self.assertEqual(countManipulations('sodo', 'domo'), [1,1])

    def test_case_3(self):
        self.assertEqual(countManipulations('todos', 'to'), -1)

    def test_case_4(self):
        self.assertEqual(countManipulations('mbja', 'paja'), [2,2])

    def test_case_5(self):
        self.assertEqual(countManipulations('mojo', 'xxoj'), [2,2])

    def test_case_6(self):
        self.assertEqual(countManipulations('mmmo', 'nnno'), [3,3])
    

if __name__ == '__main__':
    unittest.main()
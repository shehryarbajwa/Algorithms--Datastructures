
#   If currentSum > targetSum:
#   Then we have to move the right pointer, since if we move the left pointer,
#   The sum will get even bigger than what we have now.

#   Similarly, if we get a currentSum that is smaller than the targetSum:
#   Then we move the left Pointer because we want a bigger sum.
#   Think of it this way. If we start from Brampton to Toronto.

#   Brampton to Toronto is 100 Km.
#   Our target sum is 100 KM.
#   Brampton = 0, Oakville = 10, Etobicoke = 100
#   Mississauga is after Oakville at 20 km and before Etobicoke there is College Town at 70 KM
#   So If our route's total is 110, and we go through Oakville, it gets 120
#   Instead we should remove Etobicoke and go through College and the sum will become 80
#   Now at 80 we can add Mississauga and our target will be 100
#   In this fashion we have to find three routes that allows us to get to Toronto in 100 KM.

#   Only once we have traversed through the entire list, we change the currentNumber
#   We have traversed a list only when left index > right_index because at this point both numbers from left and right have merged

# O(N^2) because we iterate over the list and the while loop iterates over the remainder numbers
# Space O(1) best case if no triplets found
# O(N) for average and worst case since we might have to store all elements of the original array

import unittest


def three_number_sum(array, targetSum):
    array.sort()
    triplets = []

    #Why -2 because always need a left poitner, right pointer
    #Current number goes to a max of len(array) - 2 so that we can use left and right to traverse through the remaining numbers
    for i in range(len(array) - 2):
        current_number = array[i]
        left = i + 1
        right = len(array) - 1

        while left < right:
            current_sum = current_number + array[left] + array[right]

            if current_sum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < targetSum:
                left += 1
            else:
                right -= 1

    return triplets

    

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(three_number_sum([1,2,3,5,6,-6,-8,12], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])

if __name__ == '__main__':
    unittest.main()



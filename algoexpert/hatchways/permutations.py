import unittest

#Time complexity O(N*N *N!)
#Space complexity O(N*N*N!)

def get_permutations(array):

    if len(array) == 0:
        return []
    final_permutations = []
    permutations_helper(array, [], final_permutations)
    return final_permutations

def permutations_helper(array, single_permutation, final_permutations):
    if len(array) == 0:
        final_permutations.append(single_permutation)

    else:
        for i in range(len(array)):
            #Remove from array till i from left. Then from i exclusive from right
            array_after_remove_from_array = array[:i] + array[i+1:]
            #Add the current number to a potential permutation
            current_permutation = single_permutation + [array[i]]
            #Start breaking down the rest of the array.
            #We start with the first number as one permutation
            permutations_helper(array_after_remove_from_array, current_permutation, final_permutations)


# 1-Lets say we are given an array [1,2,3]
# 2-We will create one final permutation array to hold all unique permutations of the provided array
# 3-Then we start recursing on the input array
# 4-We choose recursion to do this because we will be computing a huge number of unique possibilities by re-arranging different numbers in the input array.
# 5-We start by looping through all indexes in the array.
# 6-In the case of 1,2,3, we will have 0,1,2 as indices in the first iteration
# 7-In index 0 , we remove the index being iterated over from the array.
# 8-Then we add the number we removed to a temporary array, which is an incomplete permutation
# 9-Now we have broken down the original array into a smaller sub-array while we are still on the first_index at 0
# 10-After we have created a temporary permutation, we have also divided our array into one smaller sub-array after removing the element at index 0.
# 11-We will now recurse on the remaining sub-array
# 12-Keep in mind, we are still at index 0 of our original array which is [1,2,3]
# 13-The remaining sub-array for index 0 iteration is [2,3]
# 14-We repeat the same steps.
# 15-Loop through the indices in the sub-array
# 16-We have indices 0 and 1
# 17-We remove the array at index 0. Array is now just [3]
# 18-We add [2] to a temporary permutation which previously was [1] so now it is [1,2]
# 19-We recurse again on the remaining sub-array which is just [3]
# 20-We are now on original index 0, second index 0, and now we only have [3] so 1 index which is 0.
# 21-We remove the number from the array at 0 which is [3]
# 22-We add it to our temporary_permutation of [1,2] which becomes [1,2,3]
# 23-Remember we can add two arrays as long as they are both arrays [1] + [2] = [1,2]
# 24-Now we have no-subarray left so now it is an empty array
# 25-We can finally add this to our final permutation array as [1,2,3]
# 26-Now we backtrack to original array's index 0, then index 1.
# 27-We repeat the same steps. Instead now, we remove element at index 1 which was [2,3] so we remove 3
# 28-We are left with [2] as array
# 29- Our temporary_permutation becomes [1,3]
# 30-We recurse again on the array [2]
# 31-We remove it at index 0
# 32-We add this to our temporary_permutation which becomes [1,3,2]
# 33-Since this array is now empty, we can add it to our final permutations
# 34-Now we are just done with index 0 of our original array [1,2,3] so we now start with index 1

#Time Complexity is O(N) for iterating through array indices
#O(N) for removing elements from the array since we have to traverse the entire array to remove
#O(N!) for appending to the final permutation array
#So worst case is O(n*n*n!)
#Best case is only 1 number so we dont 

#Space complexity is O(N * N!)
#It is n! for appending to the final permutation array which is an additional array from the input array
#We are storing n! entries in the final permutation array
#all these entries have length n
#Even though we are using recursion, we are making n recursive calls.
#Thus our recursive call stack is o(N) which fades to a higher complexity of O(N*N!)



class Test(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(get_permutations([1,2]),[[1,2],[2,1]])
    
    def test_case_2(self):
        self.assertEqual(get_permutations([1,2,3]),[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

    def test_case_3(self):
        self.assertEqual(get_permutations([1,2,3,4]),[[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]])


if __name__ == "__main__":
    unittest.main()
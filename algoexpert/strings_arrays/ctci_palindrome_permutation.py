
#Time complexity : O(n) We traverse over the given string s with n characters once. We also traverse over the mapmap which can grow upto a size of nn in case all characters in ss are distinct.
#Space complexity : O(n) The hashmap can grow upto a size of n, in case all the characters in ss are distinct.
#At best case hash map has n/2 items which is still n.
def palindrome_permutation(string):    
    count = {}

    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    count_values = list(count.values())

    count = 0

    for i in range(len(count_values)):
        count += count_values[i] % 2

    return count <= 1


    
print(palindrome_permutation('aaaabbde'))
print(palindrome_permutation('tact coa'))
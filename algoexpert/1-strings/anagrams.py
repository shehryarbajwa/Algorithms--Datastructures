
#Time Complexity O(nlogn)
#Space Complexity O(1)
def are_anagrams(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)

    return s1 == s2

def are_anagrams_hash(s1, s2):
    count = {}
    for char in s1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for char in s2:
        if char in count:
            count[char] -= 1
        else:
            count[char] = 1
    
    for value in count.values():
        if value >= 1:
            return False
    return True


print(are_anagrams_hash('act','ncnncnc'))



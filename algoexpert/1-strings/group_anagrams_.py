
#Space Complexity O(N)
#Time Complexity O(N log n)
def group_anagrams(array):
    count = {}
    for word in array:
        key = "".join(sorted(word))
        if key in count:
            count[key].append(word)
        else:
            count[key] = [word]
    
    return list(count.values())

print(group_anagrams(["yo", "act", "flop", "tac", "cat", "oy", "olfp"]))


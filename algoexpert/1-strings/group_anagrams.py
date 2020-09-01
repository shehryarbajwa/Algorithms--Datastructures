# Time Complexity O(W * n log n + n * w log w)
# Space Complexity O(n * w)
def group(words):
    sorted_words = []
    for word in words:
        sorted_words.append(("".join(sorted(word))))
    
    indices = [i for i in range(len(words))]
    indices.sort(key=lambda x: sorted_words[x])

    result = []
    anagram_group = []
    current_anagram = sorted_words[indices[0]]

    for index in indices:
        word = words[index]
        sorted_word = sorted_words[index]

        if sorted_word == current_anagram:
            anagram_group.append(word)
            continue

        result.append(anagram_group)
        anagram_group = [word]
        current_anagram = sorted_word
    #While the last iteration, there will be one group not appended to result
    result.append(anagram_group)

    return result
# Time Complexity O(w * n log(n))
# Space Complexity O(nw)
def group_anagrams(words):
    anagram = {}
    for word in words:
        sorted_word = "".join((sorted(word)))

        if sorted_word in anagram:
            anagram[sorted_word].append(word)
        else:
            anagram[sorted_word] = [word]
    return anagram

#print(group(["yo", "act", "flop", "tac", "cat", "oy", "olfp"]))
print(group_anagrams(["yo", "act", "flop", "tac", "cat", "oy", "olfp"]))
    

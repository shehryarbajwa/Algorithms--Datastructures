

def longest_duplicate_substring(string):
    if len(string) == 0:
        return 0
    last_seen = {}
    startIdx = 0
    longest = [0,1]

    for i, char in enumerate(string):
        if char in last_seen:
            startIdx = max(startIdx, last_seen[char] + 1)
        
        if longest[1] - longest[0] < i + 1 - startIdx:
            longest = [startIdx, i + 1]

        last_seen[char] = i
    
    return longest[1] - longest[0]

print(longest_duplicate_substring('pwwkew'))
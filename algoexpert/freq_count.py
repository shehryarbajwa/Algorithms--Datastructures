
def check_frequency(s1, s2):
    count = {}

    for char in s1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in s2:
        if char in count:
            return "YES"
        else:
            continue
    return "NO"

print(check_frequency('wouldyoulikefries', 'abcabcabcabcabcabc'))
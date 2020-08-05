# abc cba - permutation
# noilo olino - permutation

def is_permutation(s1, s2):
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
        if value != 0:
            return False
    return True

print(is_permutation('abc', 'cba'))
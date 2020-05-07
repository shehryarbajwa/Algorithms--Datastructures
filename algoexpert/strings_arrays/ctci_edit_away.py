
def check_edit_away(s1, s2):
    if (len(s1) != len(s2)):
        is_edit_away_insertion_deletion(s1, s2)
    
    insertion_hash = {}

    for char in s1:
        if char in insertion_hash:
            insertion_hash[char] += 1
        else:
            insertion_hash[char] = 1

    for char in s2:
        if char in insertion_hash:
            insertion_hash[char] -= 1
        else:
            insertion_hash[char] = 1

    count = 0
    value_list = list(insertion_hash.values())
    
    for i in range(len(value_list)):
        if value_list[i] == abs(1):
            count += 1
    
    return count <= 2


def is_edit_away_insertion_deletion(s1, s2):

    difference = abs(len(s1) - len(s2))

    if difference > 1:
        return False

    insertion_hash = {}

    for char in s1:
        if char in insertion_hash:
            insertion_hash[char] += 1
        else:
            insertion_hash[char] = 1
    
    for char in s2:
        if char in insertion_hash:
            insertion_hash[char] -= 1
        else:
            insertion_hash[char] = 1
    count = 0
    value_list = list(insertion_hash.values())
    print(insertion_hash)

    for i in range(len(value_list)):
        if value_list[i] == abs(1):
            count += 1
    return count <= 1

print(check_edit_away('pale', 'bake'))
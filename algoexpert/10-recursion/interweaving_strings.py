

def interweaving_strings(one, two, three):

    if len(three) != len(one) + len(two):
        return False

    hash_map = {}
    for char in one:
        if char in hash_map:
            hash_map[char] += 1
        else:
            hash_map[char] = 1
    
    for char in two:
        if char in hash_map:
            hash_map[char] += 1
        else:
            hash_map[char] = 1
    
    for char in three:
        if char in hash_map:
            hash_map[char] -= 1
        else:
            hash_map[char] = 1

    for value in hash_map.values():
        if value > 0:
            return False
        else:
            return True

def recursive_interwoven(one, two, three):
    # Write your code here.
    if len(three) != len(one) + len(two):
		return False
	return are_interwoven(one, two, three, 0,0)

def are_interwoven(one, two, three, i, j):
	k = i + j
	if k == len(three):
		return True
	
	if i < len(one) and one[i] == three[k]:
		if are_interwoven(one,two,three, i + 1, j):
			return True
	
	if j < len(two) and two[j] == three[k]:
		return are_interwoven(one,two,three, i, j + 1)
	
	return False
print(interweaving_strings('algoexpert', 'yourdreamjob', 'youralgodreamexpertjob'))


    

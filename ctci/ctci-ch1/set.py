#[0,1,2,3] -> 4

def diff_number(arr):
    new_set = set()

    for i in range(len(arr)):
        new_set.add(arr[i])
    
    for i in range(len(arr)):
        if i not in new_set:
            return i
    return i + 1

print(diff_number([0,1,2,3,5]))
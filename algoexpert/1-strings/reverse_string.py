

def reverse_string(string):
    string = [x for x in string]
    print(string)
    left = 0
    right = len(string) - 1

    while left < right:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1
    return "".join(string)

print(reverse_string('abcd'))


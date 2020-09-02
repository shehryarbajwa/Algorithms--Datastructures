
#Time Complexity O(N)
#Space Complexity O()
def reverse_string_recursion(string):
    if string == "":
        return string
    else:
        return string[-1] + reverse_string_recursion(string[:-1])

print(reverse_string_recursion('abcde'))



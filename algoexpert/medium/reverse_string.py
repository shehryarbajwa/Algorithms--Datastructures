def reverse_string(string):
    reverse = ''
    i = len(string) - 1
    while i >= 0:
        reverse += string[i]
        i -= 1
    return reverse

print(reverse_string('Shehryar'))

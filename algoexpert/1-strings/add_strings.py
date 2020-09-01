def add_strings(s1, s2):
    remainder = 0
    res = []

    p1 = len(s1) - 1
    p2 = len(s2) - 1

    while p1 >= 0 and p2 >= 0:
        x1 = ord(s1[p1]) - ord('0') if p1 >= 0 else 0
        x2 = ord(s2[p2]) - ord('0') if p2 >= 0 else 0
        add = (x1 + x2 + remainder) % 10
        remainder = (x1 + x2 + remainder) // 10
        res.append(add)
        p1 -= 1
        p2 -= 1

    if remainder != 0:
        res.append(0)

    new_res = ""
    for x in res:
        new_res += str(x)
    
    return new_res[::-1]
print(add_strings('16','19'))
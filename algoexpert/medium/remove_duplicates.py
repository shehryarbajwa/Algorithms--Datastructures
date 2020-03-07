def remove_duplicates(list1, list2):
    lhs = [x for x in list1 if x not in list2]
    rhs = [x for x in list2 if x not in list1]

    return lhs, rhs

print(remove_duplicates(['Awais', 'Shehryar', 'Rameen'], ['Awais', 'Shehryar', 'Abdullah']))
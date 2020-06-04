def validate_bst(tree):
    min_value = float('-inf')
    max_value = float('inf')
    return bst_validate_helper(tree, min_value, max_value)

def bst_validate_helper(tree, min_value, max_value):
    if tree is None:
        return True
    #First condition for right side
    #Second condition for left side
    if tree.value < min_value or tree.value >= max_value:
        return False
    left_is_valid = bst_validate_helper(tree.left, min_value, tree.value)
    right_is_valid = bst_validate_helper(tree.right, tree.value, max_value)
    return left_is_valid and right_is_valid

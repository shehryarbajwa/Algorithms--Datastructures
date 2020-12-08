

def find_mode(root):
    if not root:
        return None
    count = {}

    def visit(node):

        if not node:
            return

        if node.val in count:
            count[node.val] += 1
        else:
            count[node.val] = 1

        visit(node.left)
        visit(node.right)
    
    visit(root)
    
    max_value = float('-inf')
    mode = None

    for key, value in count.items():
        if value > max_value:
            max_value = value
            mode = key
    return mode




        


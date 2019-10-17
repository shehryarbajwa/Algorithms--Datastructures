# Task: do in-order traversal
# We want to traverse the left subtree, then visit the node, and then traverse the right subtree.

from depth_first_search_pre_order import Tree, Node, State, Stack, tree

def in_order_dfs(tree):
    visited_list = list()
    root = tree.get_root()

    def traverse(node):
        if node:

            #In in_order, we traverse the left side first

            traverse(node.get_left_child())

            #Visit the node

            visited_list.append(node.get_value())

            #Traverse the right side

            traverse(node.get_right_child())

    traverse(root)
    return 'The visit order is ' + str(visited_list)
 
print(in_order_dfs(tree))
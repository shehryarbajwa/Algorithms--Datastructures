#Traverse left subtree, then right subtree, and then visit the node.

from  depth_first_search_pre_order import Tree, Stack, Node, State, tree


def post_order_search(tree):
    visited_list = list()
    root = tree.get_root()

    def traverse(node):
        if node:

            #Traverse the left subtree

            traverse(node.get_left_child())

            #Traverse the right subtree

            traverse(node.get_right_child())

            #Visit the node

            visited_list.append(node.get_value())

    traverse(root)
    return 'The visit order is ' + str(visited_list)

print(post_order_search(tree))
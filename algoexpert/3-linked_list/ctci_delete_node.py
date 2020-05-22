
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def delete_node(node):

    if node is None or node.next is None:
        return False

    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next

    return True

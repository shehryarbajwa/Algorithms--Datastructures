# Binary search tree allows us to do insertion, search and deletion
# We can do insertion in log(n) since we have to traverse first and then check where to insert
# Similarly, search is a log(n) function since we have to traverse first either left or right to find the value we are looking for


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def set_right_child(self, Node):
        self.right = Node

    def set_left_child(self, Node):
        self.left = Node
    
    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def has_left_child(self):
        return self.left != None
        
    def has_right_child(self):
        return self.right != None

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"
        
class Tree(object):
    def __init__(self, value):
        self.root = Node(value)
    
    def get_root(self):
        return self.root

    def set_root(self, value):
        self.root = Node(value)

    def compare(self, node, new_node):

        #We try to compare the new node passed in aswell as the node being compared
        #We use node instead of root, because we will be calling compare on the sub-trees aswell
        #Therefore it makes sense to use node and get its value rather than getting the root
        
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1
    
    def insert_with_loop(self, new_value):
        new_node = Node(new_value)
        node = self.get_root()

        if node == None:
            self.root = Node(new_value)
            return
        
        while(True):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                #Override the root's value
                #The original node might have pointers to the left and right child
                #If we do node = new_node, it will lose its pointers
                node.set_value(new_node.get_value())
                break #inserted node, stop looping
            
            elif comparison == -1:
                #Traverse left
                #Insert left
                if node.has_left_child():
                    node = node.get_left_child()
                    #At this point ^, we return back to the while loop and now the node is the new value which is the left child of the root
                    #We run the while loop again, compare the left child value with new value
                    #If comparison is -1, we then check again whether it has another left child
                    #If it does, we run the loop again, otherwise, we set the child and return
                else:
                    #We will set the left child with the new node
                    node.set_left_child(new_node)
                    #When we call break the while loop will finish looping
                    break #inserted node, stop looping
            
            else:
                #The same logic goes here.
                #If comparison is +1, then we traverse right
                #We check if the node has a right child
                #If it does, we get the right child value
                #And start the while loop again
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    #If there is no right child after running the loop once or multiple times
                    #we then set the right child and break the loop
                    node.set_right_child(new_node)
                    break #inserted node, stop looping

        #For insertion with recursion, imagine original tree being root 5 left child 4, right child 6
        #We start with new_value to be 2
        # 1- self.insert_recursively(5, 2)
        # 2- comparison leads to -1
        # 3- We realize node_has_left_child of 4
        # 4-    Now we run self.insert_recursively again with values (4, 2)
        # 5-    Comparison is -1 again
        # 6-    Since no left child, we set left_child(2)
        # 7- We come back to original function since we are executing only if else logic, our loop ends
        # 8- Function is finished
        def insertion_with_recursion(self, new_value):

            if self.root.get_root() == None:
                self.set_root(new_value)
                return
            
            self.insert_recursively(self.get_root(), Node(new_value))

        def insert_recursively(self, node, new_node):
            comparison = self.compare(node, new_node)

            if comparison == 0:
                #Override the root node
                node.set_value(new_node.get_value())

            elif comparison == -1:
                if node.has_left_child():
                    self.insert_recursively(node.get_left_child(), new_node)
                else:
                    node.set_left_child(new_node)
            else:
                if node.has_right_child():
                    self.insert_recursively(node.get_right_child(), new_node)
                else:
                    node.set_right_child(new_node)







class State(object):
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    

tree_numbers = Tree(5)
print(tree_numbers)
tree_numbers.insert_with_loop(4)
print(tree_numbers)
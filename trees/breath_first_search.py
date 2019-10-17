# We are walking down the tree one level at a time. So we start with apple at the root, and next are banana and cherry, and next is dates.
# 1) start at the root node
# 2) visit the root node's left child (banana), then right child (cherry)
# 3) visit the left and right children of (banana) and (cherry).

from collections import deque
from depth_first_search_pre_order import Tree, Node, Stack, State, tree

DoubleQueue = deque(["Monday" , "Tuesday", "Wednesday"])

DoubleQueue.append("Thursday")
DoubleQueue.appendleft("Sunday")
print(DoubleQueue)

DoubleQueue.pop()
print(DoubleQueue)

DoubleQueue.popleft()
print(DoubleQueue)

class Queue():
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.appendleft(value)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.queue)


    def __repr__(self):
        if len(self.queue) > 0:
            s = "<enqueue here>\n______________\n"
            s += "\n_____________\n".join([str(item) for item in self.queue])
            s += "\n_____________\n<deque here>"
            return s
        else:
            return "<queue is empty>"


q = Queue()
q.enqueue('Apple')
q.enqueue("Banana")
q.enqueue("Cherry")
q.enqueue("Dates")
q.dequeue()
print(q)


def breadth_first_search(tree):
    #Start with creating an empty queue
    q = Queue()
    #Create an emtpy array which will contain the visiting order
    visit_order = list()
    #Get the root value of the Tree which is Apple
    node = tree.get_root()
    #Add the root to the queue. It now has q = (["Apple"])
    q.enqueue(node.get_value())

    #Check while the queue is not empty. When it is empty, it means all elements have been visited
    
    while len(q) > 0:
        #Dequeue the last element
        #Remember in a queue we remove the last in first out
        #So we start with apple and we want to remove Apple now
        node = q.dequeue()
        #Node's value is Apple
        #Visit_order now represents Apple and since Apple is visited we can remove it from the queue
        visit_order.append(node)

        #Next we check whether apple has a left child
        #We add Banana to the queue
        # Now the queue is (["Banana"])
        if node.has_left_child():
            q.enqueue(node.get_left_child())
        #We check whether root i.e Apple has a right child
        #We add Cherry to the queue
        #Queue is (["Cherry", "Banana"])
        if node.has_right_child():
            q.enqueue(node.get_right_child())

        #Since q's length is now 2 we run the while loop again
        #In the next iteration, we get the node value now which is "Banana"
        #We add Banana to the visit order
        #We check whether Banana has a left child
        #Since it does we add Dates to the queue
        #Now queue is (["Dates", "Cherry"])
        #Banana doesnt have a right node
        #We continue
        #Next node's value now is Cherry since it is the index value at -1
        #We add Cherry to visit order
        #Visit order is ["Apple", "Banana", "Cherry"]
        #We check if Cherry has a left node or right node
        #Since they are none, we continue
        #Queue is still (["Dates"])
        #node's value becomes Dates
        #Append to visit order
        #Visit order becomes ["Apple", "Banana", "Cherry", "Dates"]
        #Since Dates has no left or right child we continue and now the while loop is finished

        return visit_order
        
breadth_first_search(tree)


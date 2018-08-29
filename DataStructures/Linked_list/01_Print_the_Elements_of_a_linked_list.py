
class Node(object):

## linked list basic 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def print_list(head):
    if head:
        print(head.data)
        print_list(head.next)



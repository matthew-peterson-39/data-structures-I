####API####
# insert - add node to beginning (or end)
# search - find and return a given node
# remove - remove a given node
# size - return number of nodes
# is_empty - True if no nodes, False otherwise

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)  # creates a new node with the value we want to insert
        old_node = self.head    # create new variable to hold previous node 
        self.head = new_node  
        self.head.next = old_node

    def search(self, value_to_find):
        current_node = self.head
        while current_node:
            if current_node.value == value_to_find:
                return current_node
            current_node = current_node.next
        return None

    def printList(self): 
        current_node = self.head 
        while(current_node): 
            print (current_node.value)
            current_node = current_node.next
 
    def size(self):
        if self.head is None:
            return 0
        else:
            return 1 + LinkedList.size(self)

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
        
new_list = LinkedList()
# print(new_list.is_empty())
new_list.insert(0)
new_list.insert(1)
new_list.insert(2)
new_list.insert(3)
new_list.printList()
new_list.remove(2)
new_list.printList()
# print(new_list.is_empty())
# print(new_list.search(3))
#print(new_list.search(2))
# print(new_list.head.value)
# print(new_list.head.next.value)
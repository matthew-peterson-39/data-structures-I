####API####
# enqueue - add item to beginning
# dequeue - remove and return item from end
# peek - return last item
# size - return number of items
# is_empty - True if no items, False otherwise

class Queue:

    def __init__(self):
        self.base = []

    def enqueue(self, item):
        self.base.insert(0, item)

    def dequeue(self):
        return self.base.pop()

    def peek(self):
        if self.base:
            return self.base[0]   # access last index
        return None
    
    def size(self):
        return len(self.base)

    def is_empty(self):
        if len(self.base):
            return False
        return True
    
new_queue = Queue()
print(new_queue.is_empty()) # True
new_queue.enqueue('first item')    
new_queue.enqueue('second item')
print(new_queue.is_empty()) # False
print(new_queue.peek()) #second item
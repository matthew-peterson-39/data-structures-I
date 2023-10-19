####API####
# push - add item to top
# pop - remove and return item from top
# peek - return top item
# size - return number of items
# is_empty - True if no items, False otherwise

class Stack:
    def __init__(self):
        self.base = []

    def push(self, item):
        self.base.append(item)

    def pop(self):
        return self.base.pop()

    def peek(self):
        if self.base:
            return self.base[-1]   # access last index
        return None
    
    def is_empty(self):
        if len(self.base):
            return False
        return True
    
new_stack = Stack()
print(new_stack.is_empty()) # True
new_stack.push('first item')    
new_stack.push('second item')
print(new_stack.is_empty()) # False
print(new_stack.peek()) #second item
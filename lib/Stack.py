class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items)==0

    def push(self, item):
        if len(self.items)<self.limt:
            self.items.append(item)
        else:
            print("stack is full. Cannot push item. ")

    def pop(self):
        pass

    def peek(self):
        pass
    
    def size(self):
        pass

    def full(self):
        pass

    def search(self, target):
        pass

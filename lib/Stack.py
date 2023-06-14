class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items)==0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("stack is full. Cannot push item. ")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("stack is empty. Cannot pop item. ")
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("stack is empty. Cannot peek item.")
            return None
    
    
    def size(self):
        return len(self.items)
    

    def full(self):
        return len(self.items)==self.limit
    

    def search(self, target):
        for i in reversed(range(len(self.items))):
            if self.items[i] == target:
                return len(self.items) -1 
            return -1 

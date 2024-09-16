class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item) 
        print(f"Pushed {item} to the stack")
        
    def pop(self):
        if not self.is_empty():
            removed_item = self.stack.pop()
            print(f"Removed {removed_item} from the stack")
            return removed_item
        else:
            print("Stack is empty")
            return None
        
    def peek(self):
        if not self.is_empty():
            top_item = self.stack[-1]
            print(f"Top item is {top_item}")
            return top_item   
        else:
            print("Stack is empty")
            return None
    
    def is_empty(self):
        return len(self.stack) == 0 
    
    def size(self):
        return len(self.stack) 
    
    def display(self):
        print("Stack elements: ", self.stack)        
        
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()  
stack.peek()     
stack.pop()      
stack.display()  
stack.pop()      
stack.pop()      
stack.pop()      
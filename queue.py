class Queue:
    class Node:
        data = None
        pointer = None
        
    front_pointer = None
    back_pointer = None
    length = 0
    
    def __len__(self):
        return self.length
    
    def __str__(self):
        result = '[>'
        node = self.front_pointer
        result += node.data
        result += '<'
        for i in range(len(self) - 1):
            result += ', '   
            node = node.pointer 
            result += node.data 
        result += ']'
        return result
    
    def enqueue(self, item):
        try:
            new_node = Queue.Node()
            new_node.data = item
            self.length += 1
            
            if self.back_pointer is None:
                self.front_pointer = new_node
            else:
                self.back_pointer.pointer = new_node
            self.back_pointer = new_node
            return True
        except:
            return False
    
    def dequeue(self):
        if self.front_pointer is not None:
            self.length -= 1
            popped = self.front_pointer.data
            self.front_pointer = self.front_pointer.pointer
            
            if self.front_pointer is None:
                self.back_pointer = None
            return popped
        else:
            return None
    
    def peek(self):
        if self.front_pointer is not None:
            return self.front_pointer.data
        else:
            return None
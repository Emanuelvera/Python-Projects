

class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

#Agregar elementos
    def enqueue(self, data):
        self.inbound_stack.append(data)
        self.size += 1

# Remueve un elemento
    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
            
        return self.outbound_stack.pop()
    
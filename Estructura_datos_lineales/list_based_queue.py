

class ListQueue:
    def __init__(self):
        self.item = []
        self.size = 0

    #Agregar elementos
    def enqueue(self, data):
        self.items.inser(0,data)
        self.size += 1

    # Remueve un elemento
    def dequeue(self):
        data = self.items.pop()
        self.size -= 1 
        return data
    
    #recorre la lista para saber que y cuantos elementos hay
    def traverse(self):
        total_items = self.size

        for item in range(total_items):
            print(self.items[item])



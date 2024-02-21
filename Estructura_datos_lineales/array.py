class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    # Conocer el tamaño o longitud del array
    def __len__(self):
        return len(self.items)
    
    # No devuelve la representacion en string 
    def __str__(self):
        return str(self.items)
    
    # Convierte el array en un iterador
    def __iter__(self):
        return iter(self.items)
    
    # Nos devuelve un elemento   
    def __getitem__(self, index):
        return self.items[index]
    
    # Agrega un elemento  
    def __setitem__(Self, index, new_item):
        Self.items[index] = new_item

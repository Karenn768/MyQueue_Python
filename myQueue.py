### COLAS ###

### CLASE DE UN NODO ###
class Node:
    def __init__(self, data):
        self._previous = None  # Nodo anterior
        self._next = None      # Nodo siguiente
        self._data = data      # Dato que almacena el nodo

    def get_previous(self):
        return self._previous  # Devuelve el nodo anterior

    def set_previous(self, previous):
        self._previous = previous  # Establece el nodo anterior

    def get_next(self):
        return self._next  # Devuelve el nodo siguiente

    def set_next(self, next_node):
        self._next = next_node  # Establece el nodo siguiente

    def get_data(self):
        return self._data  # Devuelve el dato almacenado en el nodo

    def set_data(self, data):
        self._data = data  # Establece el dato del nodo

    def __repr__(self):
        return f"Node(previous={self._previous}, next={self._next}, data={self._data})"
    

### CLASE DE LA COLA ###
class MyQueue:
    def __init__(self):
        self.head = None  # Cabeza de la cola
        self.last = None  # Último nodo de la cola

    def push(self, data):
        new_node = Node(data)  # Crea un nuevo nodo con el dato

        if self.head is None:  # Si la cola está vacía
            self.head = new_node  # El nuevo nodo es la cabeza
            self.last = new_node  # El nuevo nodo es también el último
        else:
            new_node.set_previous(self.last)  # El nuevo nodo apunta al anterior último nodo
            self.last.set_next(new_node)      # El último nodo apunta al nuevo nodo
            self.last = new_node              # Actualiza el último nodo a ser el nuevo nodo

    def poll(self):
        if self.head is None:  # Si la cola está vacía
            return None

        data = self.head.get_data()  # Obtiene el dato del nodo en la cabeza
        self.head = self.head.get_next()  # La cabeza ahora es el siguiente nodo

        if self.head is not None:
            self.head.set_previous(None)  # Si hay un nodo siguiente, su anterior es ahora None
        else:
            self.last = None  # Si la cabeza es None, la cola está vacía

        return data  # Retorna el dato del nodo que se eliminó

    def peek(self):
        if self.head is not None:
            return self.head.get_data()  # Retorna el dato de la cabeza sin eliminarlo
        return None

    def is_empty(self):
        return self.head is None  # Retorna True si la cola está vacía


# Ejemplo de uso
queue = MyQueue()
queue.push(10)
queue.push(20)
queue.push(30)

print("Primer elemento de la cola:", queue.peek())  # Salida: 10
print("Elemento eliminado: ", queue.poll())  # Salida: 10
print("Elemento eliminado: ", queue.poll())  # Salida: 20
print(queue.is_empty())  # Salida: False
print(queue.poll())  # Salida: 30
print(queue.is_empty())  # Salida: True

from functools import wraps
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, num = None):
        self.head = None
        self._length = 0
        
        if num:
            for item in reversed(num):
                self.insert(item)
                
    def traverse(self,action):
        current = self.head
        while current:
            action(current.value)
            current = current.next

    def __iter__(self):
        def generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return generator()

    def __str__(self):
        output = ''
        for value in self:
            output += f'[{value}] -> '
        return output + 'None'

    def __len__(self):
        return self._length

    def insert(self,value):
        self.head = Node(value,self.head)
        self._length += 1

    def __getitem__(self, idx):
        if idx < 0:
            raise IndexError
        for i, item in enumerate(self):
            if i == idx:
                return item
        raise IndexError

def proclaim(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        orig_value = function(*args, **kwargs)
        return 'form other side , ' + orig_value
    return wrapper

@proclaim
def txt(message):
    return message

if __name__ == '__main__':
    print(txt('Hello World.'))
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.map = {} 

        self.left = Node(0,0)
        self.right = Node(0,0)
        
        self.left.next = self.right 
        self.right.prev = self.left 

    def remove(self, Node):   
        prev, nxt = Node.prev, Node.next  
        prev.next = nxt
        nxt.prev = prev

    def insert(self, Node): 
        prev, nxt = self.right.prev, self.right
        prev.next = Node 
        Node.prev = prev 
        nxt.prev = Node 
        Node.next = nxt
        
        
    def get(self, key: int) -> int:
        if key in self.map: 
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map: 
            node = self.map[key]
            self.remove(node)
    
        node = Node(key, value)
        self.map[key] = node
        self.insert(node) 
      
        if len(self.map) > self.capacity: 
            node = self.left.next 
            self.remove(node)
            del self.map[node.key]










        

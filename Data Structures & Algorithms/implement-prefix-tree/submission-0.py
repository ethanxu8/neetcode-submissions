class PrefixTreeNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for chr in word: 
            if chr not in node.children: 
                node.children[chr] = PrefixTreeNode()
            node = node.children[chr]
        node.end = True
            
    def search(self, word: str) -> bool:
        node = self.root 
        for chr in word: 
            if chr not in node.children: 
                return False 
            node = node.children[chr]
        return node.end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root 
        for chr in prefix: 
            if chr not in node.children: 
                return False 
            node = node.children[chr]
        return True
        
        
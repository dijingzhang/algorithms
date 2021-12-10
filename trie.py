class Tire:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True

    def search(self, word):
        current = self.root
        for w in word:
            if w not in current.children:
                return False
            current = current.children[w]
        return current.isword
    
    def startsWith(self, prefix):
        current = self.root
        for w in prefix:
            if w not in current.children:
                return False
            current = current.children[w]
        return True

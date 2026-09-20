class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr =  curr.children[i]

        curr.end = True

    def search(self, word):
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr =  curr.children[i]

        if curr.end == True:
            return True
        else:
            return False

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr =  curr.children[i]

        return True
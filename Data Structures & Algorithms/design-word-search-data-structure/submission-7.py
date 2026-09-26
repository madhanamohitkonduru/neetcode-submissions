class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class WordDictionary:
    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.end = True
    
    def search(self, word: str) -> bool:
        q = collections.deque()
        q.append((0, self.root))

        while q:
            i, node = q.pop()

            if len(word) == i:
                if node.end==True:
                    return True
                else:
                    continue

            c = word[i]
            if c == ".":
                for child in node.children.values():
                    q.append((i+1, child))
            elif c in node.children:
                q.append((i+1, node.children[c]))
        return False
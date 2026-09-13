class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        maps ={}
        for i in range(n):
            maps[i] = []
        for k,v in edges:
            maps[k].append(v)
            maps[v].append(k)

        visited = set()
        def foo(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in maps[node]:
                if neighbor == parent:
                    continue
                if not foo(neighbor, node):
                    return False
            
            return True
        return foo(0, -1) and len(visited) == n

        
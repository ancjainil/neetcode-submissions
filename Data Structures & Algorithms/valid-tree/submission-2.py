class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!= n-1:
            return False
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        queue = deque([0])
        visited.add(0)
        while queue:
            node = queue.pop()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return len(visited)==n
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        THought process
        - This is essentially a cycle detection problem
        - Will a topological sorting work here? (Not really because these are undirected graphs. )
        - I'm think if we create a adjacency list then we can 

        Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]

        adjList = {
            0: [1, 2, 3],
            1: [0, 4],
            2: [0],
            3: [0]
        }

        """

        adj = {i: [] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)

            for nei in adj[curr]:                
                if nei == prev:
                    continue 
                
                if not dfs(nei, curr):
                    return False 
            
            return True 
        
        return dfs(0, -1) and n == len(visited)
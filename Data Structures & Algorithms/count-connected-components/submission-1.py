class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        adjList = {
            0: [1],
            1: [0, 2],
            2: [1]
            3: [4],
            4: [3]
            }

        seen = {0, 1, 2, 3, 4}
        """

        adjList = [[] for _ in range(n)]

        # Create adjList 
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)

        seen = set()  
        components = 0
    
        def dfs(node):
            seen.add(node)

            for nei in adjList[node]:
                if nei not in seen:
                    dfs(nei)

        for node in range(n):
            if node not in seen:
                dfs(node)
                components += 1

        return components

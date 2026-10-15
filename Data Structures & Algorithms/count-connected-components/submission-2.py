class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Thought process
        - Create an adjList of all the nodes and their neighbors
        - Iterate through the adjacency list and then walk all neighbours. using a dfs. 
        - Once the the dfs exits; we have iterated a connected component.
        - Ensure to keep a visisted set so that when we go to the next componenet which has already been visited by a previous connectec component we skip. 
        - At every dfs exit; we increment the connected component count. 
        - Keep doing this until we have exhasted the entire adjList
        """

        adj_list = {i: [] for i in range(n)}
        visited = set() 
        components = 0

        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for nei in adj_list[node]:
                dfs(nei)

        for node in adj_list:
            if node not in visited:
                dfs(node)
                components += 1
        
        return components
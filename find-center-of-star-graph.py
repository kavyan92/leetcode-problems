"""There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

Example 1:
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

Example 2:
Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1"""

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge_dict = {}
        for edge in edges:
            for val in edge:
                edge_dict[val] = edge_dict.get(val, 0) + 1
                
        for key, value in edge_dict.items():
            if value == len(edges):
                return key

"""Runtime: 836 ms, faster than 52.47% of Python3 online submissions for Find Center of Star Graph.
Memory Usage: 50.2 MB, less than 73.84% of Python3 online submissions for Find Center of Star Graph."""
from typing import List

# There is an undirected star graph consisting of n nodes labeled from 1 to n.
# A star graph is a graph where there is one center node and exactly n - 1 edges
# that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates
# that there is an edge between the nodes ui and vi.
# Return the center of the given star graph.

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        # Track visited nodes.
        visited = []

        # Iterate through each edge.
        for i in range(len(edges)):

            # Iterate through each node within edge.
            # If it is already within the visited list, return that
            # value as the answer as the node with >= 2 connections will
            # be the center given the definition of a star graph (we do not need
            # to check any further).
            for j in range(len(edges[0])):
                if edges[i][j] in visited:
                    return edges[i][j]
                visited.append(edges[i][j])
        return -1

"""
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.

"""
class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        # Create a set of all nodes
        all_nodes = set(range(n))
        
        # Create a set of destination nodes
        destination_nodes = set(destination for _, destination in edges)
        
        # Compute the set difference between all nodes and destination nodes
        source_nodes = all_nodes - destination_nodes
        
        # Convert the set of source nodes to a list
        return list(source_nodes)
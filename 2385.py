from collections import defaultdict, deque
from typing import Optional


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Convert binary tree to undirected graph
        graph = defaultdict(list)
        self.buildGraph(root, None, graph)

        # Perform BFS starting from the start node
        queue = deque([(start, 0)])  # (node, distance)
        visited = set([start])
        max_distance = 0

        while queue:
            node, distance = queue.popleft()
            max_distance = max(max_distance, distance)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))
                    visited.add(neighbor)

        return max_distance

    def buildGraph(self, node, parent, graph):
        if not node:
            return

        if parent:
            graph[node.val].append(parent.val)
            graph[parent.val].append(node.val)

        self.buildGraph(node.left, node, graph)
        self.buildGraph(node.right, node, graph)

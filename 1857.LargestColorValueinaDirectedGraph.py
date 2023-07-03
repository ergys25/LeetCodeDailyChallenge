"""
1857
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.
"""

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n, dq, seen = len(colors), collections.deque(), set()
        nxt = [set() for _ in range(n)]
        pre = [0 for _ in range(n)]
        dicts = [{x : 1} for x in colors]
        
        for i, j in edges:
            if i == j:
                return -1
            nxt[i].add(j)
            pre[j] += 1
            
        for i in range(n):
            if not pre[i]:
                dq.append(i)
                seen.add(i)
                
        while dq:
            cur = dq.popleft()
            for cand in nxt[cur]:
                tmp = {colors[cand] : 1}
                for i, x in dicts[cur].items():
                    if i not in tmp:
                        tmp[i] = x
                    else:
                        tmp[i] += x
                for i, x in tmp.items():
                    if i not in dicts[cand]:
                        dicts[cand][i] = x
                    else:
                        dicts[cand][i] = max(dicts[cand][i], x)
                pre[cand] -= 1
                if not pre[cand] and cand not in seen:
                    seen.add(cand)
                    dq.append(cand)
                    
        if len(seen) != n:
            return -1
        
        return max(max(i.values()) for i in dicts)

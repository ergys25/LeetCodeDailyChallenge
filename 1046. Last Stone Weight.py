"""
1046

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
"""


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # convert stones to negative numbers for max heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # get the two largest stones
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)

            # smash the two stones together
            if stone1 != stone2:
                heapq.heappush(max_heap, stone1 - stone2)

        # if there is only one stone left, return its positive value
        if max_heap:
            return -max_heap[0]
        else:
            return 0

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Inserts a new interval into a list of intervals and merges overlapping intervals.

        Args:
            intervals (List[List[int]]): The list of intervals.
            newInterval (List[int]): The new interval to be inserted.

        Returns:
            List[List[int]]: The list of intervals after inserting and merging.

        """

        res = []
        i = 0

        # Case 1: No overlapping before merging intervals
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Case 2: Overlapping and merging intervals
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # Case 3: No overlapping after merging newInterval
        res.extend(intervals[i:])

        return res




# Time: O(n)
# Space: O(n)

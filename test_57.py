import pytest
from typing import List

class TestSolution:
    def test_insert(self):
        solution = Solution()

        # Test case 1: No overlapping before merging intervals
        intervals1 = [[1, 3], [6, 9]]
        newInterval1 = [2, 5]
        expected1 = [[1, 3], [2, 5], [6, 9]]
        assert solution.insert(intervals1, newInterval1) == expected1

        # Test case 2: Overlapping and merging intervals
        intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval2 = [4, 9]
        expected2 = [[1, 2], [3, 10], [12, 16]]
        assert solution.insert(intervals2, newInterval2) == expected2

        # Test case 3: No overlapping after merging newInterval
        intervals3 = [[1, 5]]
        newInterval3 = [6, 8]
        expected3 = [[1, 5], [6, 8]]
        assert solution.insert(intervals3, newInterval3) == expected3

        # Test case 4: Empty intervals list
        intervals4 = []
        newInterval4 = [1, 3]
        expected4 = [[1, 3]]
        assert solution.insert(intervals4, newInterval4) == expected4

        # Test case 5: Empty newInterval
        intervals5 = [[1, 3], [6, 9]]
        newInterval5 = []
        expected5 = [[1, 3], [6, 9]]
        assert solution.insert(intervals5, newInterval5) == expected5

if __name__ == '__main__':
    pytest.main()
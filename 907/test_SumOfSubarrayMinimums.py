import pytest
from SumOfSubarrayMinimums import Solution

class TestSumOfSubarrayMinimums:
    def test_sumSubarrayMins(self):
        obj = Solution()

        # Test case 1
        arr1 = [3, 1, 2, 4]
        assert obj.sumSubarrayMins(arr1) == 17

        # Test case 2
        arr2 = [1, 2, 3, 4, 5]
        assert obj.sumSubarrayMins(arr2) == 35

        # Test case 3
        arr3 = [5, 4, 3, 2, 1]
        assert obj.sumSubarrayMins(arr3) == 35

        # Test case 4
        arr4 = [1]
        assert obj.sumSubarrayMins(arr4) == 1

        # Test case 5
        arr5 = [1, 1, 1, 1, 1]
        assert obj.sumSubarrayMins(arr5) == 15

        # Test case 6
        arr6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert obj.sumSubarrayMins(arr6) == 220

        # Test case 7
        arr7 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        assert obj.sumSubarrayMins(arr7) == 220

if __name__ == '__main__':
    pytest.main()
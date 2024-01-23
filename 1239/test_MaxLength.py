import pytest
from MaxLength import Solution


class TestMaxLength:
    def test_maxLength(self):
        obj = Solution()

        # Test case 1
        arr1 = ["un", "iq", "ue"]
        assert obj.maxLength(arr1) == 4

        # Test case 2
        arr2 = ["cha", "r", "act", "ers"]
        assert obj.maxLength(arr2) == 6

        # Test case 3
        arr3 = ["abcdefghijklmnopqrstuvwxyz"]
        assert obj.maxLength(arr3) == 26

        # Test case 4
        arr4 = ["aa", "bb", "cc", "dd"]
        assert obj.maxLength(arr4) == 0

        # Test case 5
        arr5 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                "y", "z"
                ]
        assert obj.maxLength(arr5) == 26


if __name__ == '__main__':
    pytest.main()

import pytest
from minFallingPathSum import Solution

class TestMinFallingPathSum:
    def test_minFallingPathSum(self):
        obj = Solution()  

        # Test case 1
        matrix1 = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
        assert obj.minFallingPathSum(matrix1) == 12

        # Test case 2
        matrix2 = [[-1, -2, -3],
                   [-4, -5, -6],
                   [-7, -8, -9]]
        assert obj.minFallingPathSum(matrix2) == -18

        # Test case 3
        matrix3 = [[1]]
        assert obj.minFallingPathSum(matrix3) == 1

        # Test case 4
        matrix4 = [[-1]]
        assert obj.minFallingPathSum(matrix4) == -1

        # Test case 5
        matrix5 = [[1, 2],
                   [3, 4]]
        assert obj.minFallingPathSum(matrix5) == 4

        # Test case 6
        matrix6 = [[-1, -2],
                   [-3, -4]]
        assert obj.minFallingPathSum(matrix6) == -6

        # Test case 7
        matrix7 = [[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]]
        assert obj.minFallingPathSum(matrix7) == 28

        # Test case 8
        matrix8 = [[-1, -2, -3, -4],
                   [-5, -6, -7, -8],
                   [-9, -10, -11, -12],
                   [-13, -14, -15, -16]]
        assert obj.minFallingPathSum(matrix8) == -40

if __name__ == '__main__':
    pytest.main()

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        max_product = [0] * (n + 1)

        max_product[1] = 1
        max_product[2] = 2
        max_product[3] = 3

        for num in range( 4, n + 1 ):
            max_product_for_num = 0
            for sub_num in range(1, num // 2 + 1):
                max_product_for_num = max(max_product_for_num, max_product[sub_num] * max_product[num - sub_num])
            max_product[ num ] = max_product_for_num

        return max_product[ n ]


# The  space  complexity of the code is O(n) because we are creating an array of size n+1 to store the maximum product for each number from 1 to n.

# The  time complexity of the code is O(n^2) because we are using a nested loop to calculate the maximum product for each number from 4 to n. The outer loop runs n-3 times, and the inner loop runs (num // 2) times, which is approximately n/2 times. Therefore, the total number of iterations is approximately (n-3) * (n/2), which is O(n^2).


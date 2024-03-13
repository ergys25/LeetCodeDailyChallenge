# URL: https://www.acmicpc.net/problem/4855
# Desc: pivot integer
# Input: n
# Output: pivot integer
# Condition: pivot integer is a number that can be expressed as the sum of consecutive positive integers
# Example: 15 -> 5 (1 + 2 + 3 + 4 + 5)
#          10 -> 3 (1 + 2 + 3 + 4)
#          20 -> 6 (2 + 3 + 4 + 5 + 6)
#          100 -> 18 (9 + 10 + 11 + 12 + 13 + 14 + 15 + 16)

# Approach:
# 1. Create a list of prefix sum
# 2. Iterate through the list and find the pivot integer
# 3. Return the pivot integer
# 4. If pivot integer is not found, return -1



class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix_sum = [1]

        for i in range(2, n + 1):
            prefix_sum.append(prefix_sum[ i - 2] + i)
        print(prefix_sum)



        if n == 1:
            return 1
        

        for i in range(1, len(prefix_sum)):
            if prefix_sum[len(prefix_sum) - 1] - prefix_sum[i -1] == prefix_sum[i]:
                return i + 1
        return -1
    # Time complexity: O(N)
    # Space complexity: O(N)
    
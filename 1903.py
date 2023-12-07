# https://leetcode.com/problems/largest-odd-number-in-string/
# Difficulty: Easy
# Date: 2021-07-24
# Submission: https://leetcode.com/submissions/detail/523000000/
# Time Taken: 20 ms
# Memory Used: 14.2 MB
# Runtime: 98.98%
# Memory: 90.37%


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""
    
    "unit test"
    def test(self):
        testCases = [
            "52",   # 5
            "4206", # ""
            "35427",# 35427 
        ]
        for i in testCases:
            print(self.largestOddNumber(i))

Solution().test()


        
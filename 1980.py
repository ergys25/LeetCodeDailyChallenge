#Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i][i] == '0':
                ans.append('1')
            else:
                ans.append('0')
        return ''.join(ans)



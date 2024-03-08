class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        map = [0] *101
        result = 0

        for n in nums:

            map[n] +=1

        k = (max(map))

        for n in map:
            if n == k:
                result += n

        return result




        
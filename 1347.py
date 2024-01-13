from collections import defaultdict


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        frequency_s = defaultdict(int)
        frequency_t = defaultdict(int)
        result = 0

        for i in range(len(s)):
            frequency_s[s[i]] += 1
            frequency_t[t[i]] += 1

        for key in frequency_s.keys():
            if frequency_s[key] > frequency_t[key]:
                result += frequency_s[key] - frequency_t[key]

        return result

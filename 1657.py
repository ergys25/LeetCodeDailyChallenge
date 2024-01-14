from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) == set(word2):
            c1 = Counter(word1)
            c2 = Counter(word2)
            d1 = []
            d2 = []

            for key in c1.keys():
                d1.append(c1[key])

            for key in c2.keys():
                d2.append(c2[key])

            d1.sort()
            d2.sort()

            return d1 == d2

        else:
            return False

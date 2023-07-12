"""
1456.py
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        max_vowels = curr_vowels = 0
        for i, c in enumerate(s):
            if i >= k and s[i-k] in vowels:
                curr_vowels -= 1
            if c in vowels:
                curr_vowels += 1
            max_vowels = max(max_vowels, curr_vowels)
        return max_vowels

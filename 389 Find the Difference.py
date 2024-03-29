# You are given two strings s and t.

# String t is generated by random shuffling string s and then add one more letter at a random position.

# Return the letter that was added to t.

#steps
#1. create a dictionary of the letters in s
#2. iterate through t, if the letter is not in the dictionary, return the letter
#3. if the letter is in the dictionary, subtract 1 from the value
#4. if the value is 0, remove the letter from the dictionary

#time: O(n)
#space: O(n)
#runtime: 32 ms, faster than 77.65% of Python3 online submissions for Find the Difference.
#Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Find the Difference.


 


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = {} # O(1)
        
        for letter in s:    # O(n)
            if letter not in letters:   # O(1)
                letters[letter] = 1     # O(1)
            else:       # O(1)
                letters[letter] += 1    # O(1)
        
        for letter in t:    # O(n)
            if letter not in letters:   # O(1)
                return letter       # O(1)
            else:       # O(1)
                letters[letter] -= 1    # O(1)
                if letters[letter] == 0:    # O(1)
                    del letters[letter]    # O(1)
        
        return None # O(1)

        
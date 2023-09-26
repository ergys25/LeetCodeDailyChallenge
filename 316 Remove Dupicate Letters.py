from collections import Counter


class Solution:
    

# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
# the smallest in lexicographical order
#  among all possible results.

# Steps:
# 1. Use Counter to count the frequency of each letter
# 2. Use a stack to store the letters
# 3. Iterate through the string, if the letter is not in the stack, check if the letter is smaller than the top of the stack and
#    the top of the stack still has frequency left. If so, pop the top of the stack and add the letter to the stack.
# 4. Return the stack as a string

    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s) # O(n)
        stack = [] # O(n)
        
        for letter in s: # O(n)
            if letter not in stack:# O(1)
                while stack and letter < stack[-1] and counter[stack[-1]] > 0: # O(1)
                    stack.pop()# O(1)
                stack.append(letter)# O(1)
            counter[letter] -= 1# O(1)
        
        return ''.join(stack)# O(n) 




# Time: O(n)
# Space: O(n)
# Runtime: 32 ms, faster than 77.65% of Python3 online submissions for Remove Duplicate Letters.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Remove Duplicate Letters.





    
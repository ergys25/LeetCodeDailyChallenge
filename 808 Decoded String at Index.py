# You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

# If the character read is a letter, that letter is written onto the tape.
# If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
# Given an integer k, return the kth letter (1-indexed) in the decoded string.

# Steps
# 1. create a stack
# 2. iterate through the string
# 3. if the character is a letter, add it to the stack
# 4. if the character is a number, multiply the stack by the number
# 5. if the stack is greater than k, return the kth letter

# time: O(n)
# space: O(n)
# runtime: 28 ms, faster than 92.94% of Python3 online submissions for Decoded String at Index.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Decoded String at Index.

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = [] # O(1)
        
        for char in s: # O(n)
            if char.isalpha(): # O(1)
                stack.append(char) # O(1)
            else: # O(1)
                stack = stack * int(char) # O(1)
        
        if len(stack) >= k: # O(1)
            return stack[k-1] # O(1)
        
        return None # O(1)
    
